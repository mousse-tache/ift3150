"""
.. moduleauthor:: Eugene Syriani
.. moduleauthor:: Florin Oncica 

.. versionadded:: 1.0

Created on Nov 09, 2016

This module contains all the commands of BiBler.
It implements the Command design pattern.
"""

from .impex import BibTeXImporter, CSVImporter, EndNoteImporter, BibTeXExporter, CSVExporter, HTMLExporter, MySQLExporter
from .entry import EntryIdGenerator
from utils import settings
from utils.settings import Preferences


class CommandExecutor(object):
    def __init__(self):
        """
        (Constructor)
        """
        self.__history = []
    
    def execute(self, command):
        result = command.execute()
        if isinstance(command, OpenCommand):
            self.__history = [command]    # cannot undo further than the last open command
        elif isinstance(command, UndoableCommand):
            # Only add undoable commands to history and only after command is complete
            self.__history.append(command)
        return result
    
    def canUndo(self):
        return len(self.__history) > 0
    
    def undo(self):
        if self.canUndo():
            last_command = self.__history.pop()
            last_command.unexecute()
            return True
        return False


class Command(object):
    def __init__(self, manager):
        """
        (Constructor)
        """
        self.manager = manager


class UndoableCommand(Command):
    def __init__(self, manager):
        """
        (Constructor)
        """
        super(UndoableCommand, self).__init__(manager)


class UndoCommand(Command):
    def __init__(self, invoker):
        """
        (Constructor)
        """
        super(UndoCommand, self).__init__(None)
        self.invoker = invoker
    
    def execute(self):
        return self.invoker.undo()


class PreviewCommand(Command):
    def __init__(self, manager, entryId):
        """
        (Constructor)
        """
        super(PreviewCommand, self).__init__(manager)
        self.entryId = entryId
    
    def execute(self):
        entry = self.manager.getEntry(self.entryId)
        if entry:
            if Preferences().bibStyle == settings.BibStyle.ACM:
                return entry.toCompleteHtmlACM()
            else:
                return entry.toCompleteHtmlDefault()
        raise Exception('entry not found.')


class ExportCommand(Command):
    def __init__(self, manager, path, exportFormat):
        """
        (Constructor)
        """
        super(ExportCommand, self).__init__(manager)
        self.path = path
        self.exportFormat = exportFormat
        self.total = 0
    
    def execute(self):
        if self.exportFormat == settings.ExportFormat.BIBTEX:
            exporter = BibTeXExporter
        elif self.exportFormat == settings.ExportFormat.CSV:
            exporter = CSVExporter
        elif self.exportFormat == settings.ExportFormat.HTML:
            exporter = HTMLExporter
        elif self.exportFormat == settings.ExportFormat.SQL:
            exporter = MySQLExporter
        self.total = exporter(self.path, self.manager.iterEntries()).export()
        return self.total > 0

class GenerateAllKeysCommand(Command):
    def __init__(self, manager):
        """
        (Constructor)
        """
        super(GenerateAllKeysCommand, self).__init__(manager)
    
    def execute(self):
        return self.manager.generateAllKeys()

class ValidateAllCommand(Command):
    def __init__(self, manager):
        """
        (Constructor)
        """
        super(ValidateAllCommand, self).__init__(manager)
    
    def execute(self):
        # True is automatically cast to 1 and False to 0
        return sum([entry.validate().isValid() for entry in self.manager.iterEntries()])


class SearchCommand(Command):
    def __init__(self, manager, query):
        """
        (Constructor)
        """
        super(SearchCommand, self).__init__(manager)
        self.query = query
    
    def execute(self):
        return self.manager.search(self.query)


class AddCommand(UndoableCommand):
    def __init__(self, manager, entryBibTeX, entryType):
        """
        (Constructor)
        """
        super(AddCommand, self).__init__(manager)
        self.entryBibTeX = entryBibTeX
        self.entryType = entryType
        self.entryId = 0
    
    def execute(self):
        self.entryId = self.manager.add(self.entryBibTeX, self.entryType)
        return self.entryId
    
    def unexecute(self):
        return self.manager.delete(self.entryId)


class DeleteCommand(UndoableCommand):
    def __init__(self, manager, entryId):
        """
        (Constructor)
        """
        super(DeleteCommand, self).__init__(manager)
        self.entryId = entryId
        self.originalEntry = None
        self.originalEntryIndex = 0
    
    def execute(self):
        self.originalEntry = self.manager.getEntry(self.entryId)
        if not self.originalEntry:
            return False
        self.originalEntryIndex = self.manager.getIndex(self.originalEntry)
        return self.manager.delete(self.entryId)
    
    def unexecute(self):
        self.manager.insertAt(self.originalEntryIndex, self.originalEntry)


class DuplicateCommand(UndoableCommand):
    def __init__(self, manager, originalEntryId):
        """
        (Constructor)
        """
        super(DuplicateCommand, self).__init__(manager)
        self.originalEntryId = originalEntryId
        self.duplicatedEntryId = 0
    
    def execute(self):
        self.duplicatedEntryId = self.manager.duplicate(self.originalEntryId)
        return self.duplicatedEntryId
    
    def unexecute(self):
        return self.manager.delete(self.duplicatedEntryId)


class UpdateCommand(UndoableCommand):
    def __init__(self, manager, entryId, entryBibTeX, fieldName = None, fieldValue = None):
        """
        (Constructor)
        """
        super(UpdateCommand, self).__init__(manager)
        self.oldBibTeX = ''
        self.newBibTeX = entryBibTeX
        self.entryId = entryId
        self.fieldName = fieldName
        self.fieldValue = fieldValue
    
    def execute(self):
        entry = self.manager.getEntry(self.entryId)
        if entry:
            self.oldBibTeX = entry.toBibTeX()
        else:
            return False
        if (self.fieldName == None and self.fieldValue == None):
            return self.manager.update(self.entryId, self.newBibTeX)
        else:
            return self.manager.updateEntryField(self.entryId, self.fieldName, self.fieldValue)
    
    def unexecute(self):
        return self.manager.update(self.entryId, self.oldBibTeX)


class ImportCommand(UndoableCommand):
    def __init__(self, manager, path, importFormat):
        """
        (Constructor)
        """
        super(ImportCommand, self).__init__(manager)
        self.path = path
        self.importFormat = importFormat
        self.manager = manager
        self.lastId = EntryIdGenerator().getLastId()
        self.total = 0
    
    def execute(self):
        if self.importFormat == settings.ImportFormat.BIBTEX:
            importer = BibTeXImporter
        elif self.importFormat == settings.ImportFormat.CSV:
            importer = CSVImporter
        elif self.importFormat == settings.ImportFormat.ENDNOTE:
            importer = EndNoteImporter
        self.total = importer(self.path, self.manager).importFile()
        return self.total > 0
    
    def unexecute(self):
        for i in range(self.total):
            i += self.lastId + 1
            if self.manager.getEntry(i):
                self.manager.delete(i)
        return True


class OpenCommand(ImportCommand):
    def __init__(self, manager, path, openFormat):
        """
        (Constructor)
        """
        super(OpenCommand, self).__init__(manager, path, openFormat)
    
    def execute(self):
        self.manager.deleteAll()
        return super(OpenCommand, self).execute()
    
    def unexecute(self):
        self.manager.deleteAll()


class SortCommand(UndoableCommand):
    def __init__(self, manager, field, reverse=False):
        """
        (Constructor)
        """
        super(SortCommand, self).__init__(manager)
        self.field = field
        self.originalEntryOrder = []     # keeps the ids in the order they were
        self.originalSearchResultOrder = []     # keeps the ids in the order they were
        self.reverse = reverse
    
    def execute(self):
        self.originalEntryOrder = [e.getId() for e in self.manager.iterEntries()]
        self.originalSearchResultOrder = [e.getId() for e in self.manager.iterSearchResult()]
        return self.manager.sort(self.field, self.reverse) 
    
    def unexecute(self):
        self.manager.entryList.sort(key=lambda e: self.originalEntryOrder.index(e.getId()))
        self.manager.searchResult.sort(key=lambda e: self.originalSearchResultOrder.index(e.getId()))
        return True
