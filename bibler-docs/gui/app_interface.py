"""
Created on Jan 13, 2014
.. moduleauthor:: Eugene Syriani
.. moduleauthor:: Florin Oncica 

.. versionadded:: 1.0

This module represents the interface that the :class:`app` module must conform to.
@group Interchange data-structures: EntryDict, EntryListColumn
@sort: EntryDict, EntryListColumn
"""

class EntryListColumn(object):
    """
    The columns of the entry list.
    """
    Author = 'author'
    Entrytype = 'entrytype'
    Entrykey = 'entrykey'
    Id = 'id'
    Message = 'message'
    Paper = 'paper'
    Title = 'title'
    Valid = 'valid'
    Year = 'year'
    
    @staticmethod
    def list():
        """
        :rtype: :class:`list`
        :return: A list of all the columns.
        """
        return [EntryListColumn.Author, EntryListColumn.Id, EntryListColumn.Entrykey, EntryListColumn.Paper,
                EntryListColumn.Title, EntryListColumn.Entrytype, EntryListColumn.Valid, EntryListColumn.Year, EntryListColumn.Message]

class EntryDict(dict):
    """
    The exchange format of entries.
    It is a dictionary where all :class:`EntryListColumn` fields are predefined keys that cannot be removed.
    
        >>> d = EntryDict()
        >>> print d
            {'id': '', ...}
        >>> del d[EntryListColumn.Id]
        >>> print d
            {'id': '', ...}
    """
    def __init__(self, *args):
        """
        All :class:`EntryListColumn` fields are predefined keys.
        """
        dict.__init__(self, args)
        for key in EntryListColumn.list():
            if key not in iter(self.keys()):
                if key == EntryListColumn.Id:
                    self[key] = 0
                else:
                    self[key] = ''
        
    def __delitem__(self, key):
        """
        Deleting a :class:`EntryListColumn` key will set its value to :class:`''`.
        """
        if key not in EntryListColumn.list():
            dict.__delitem__(key)
        elif key == EntryListColumn.Id:
            raise KeyError('Cannot delete key: ' + EntryListColumn.Id)
        else:
            self[key] = ''
        
    def toBibTeX(self):
        """
        Convert into a BibTeX reference.
        :rtype: :class:`str`
        :return: The BibTeX reference.
        :note: The BibTeX format is::
            @TYPE{KEY,
              FIELD1 = {VALUE1},
              FIELD2 = {VALUE2}
            }
        """
        try:
            bibtex = '@%s{%s' % (self[EntryListColumn.Entrytype].upper(), self[EntryListColumn.Entrykey])
            for field,value in self.items():
                if field == EntryListColumn.Id or field == EntryListColumn.Valid:
                    continue
                # This part is to put {} around capital letters if they aren't already
                v = ''
                for i in range(len(value)):
                    if value[i].isupper():
                        if 0 < i < len(value) - 1 and value[i-1] != '{' and value[i+1] != '}':
                            v += '{%s}' % value[i]
                    else:
                        v += value[i]
                bibtex += ',\n  %s = {%s}' % (field, value)
            bibtex += '\n}'
            return bibtex
        except:
            return ''
    
    @staticmethod
    def fromDict(d):
        """
        Convert a Python :class:`dict` into an :class:`EntryDict`.
        :type d: :class:`dict`
        :param d: The dictionary to convert.
        :rtype: :class:`EntryDict`
        :return: An :class:`EntryDict` with all the keys and values from :class:`d`.
        """
        ed = EntryDict()
        for k in d:
            ed[k] = d[k]
        return ed

class IApplication(object):
    """
    Interface that provides all the application functions required for the :class:`Controller<gui.controller.Controller>`.
    The meaning of every operation in the BiBler GUI is given by these functions.
    """
    
    def start(self):
        """
        Start the application.
        """
        raise NotImplementedError()
    
    def exit(self):
        """
        Close the application.
        """
        raise NotImplementedError()
    
    def importFile(self, path, importFormat):
        """
        Import a list of entries from a file in a given format.
        :type path: :class:`str`
        :param path: The path to a file.
        :type importFormat: :class:`utils.settings.ImportFormat`
        :param importFormat: The format of the file.
        :rtype: :class:`bool`
        :return: :class:`True` if succeeded, :class:`False` otherwise.
        """
        raise NotImplementedError()
    
    def exportFile(self, path, exportFormat):
        """
        Export the list of entries to a file in a given format.
        :type path: :class:`str`
        :param path: The path to a file.
        :type exportFormat: :class:`utils.settings.ExportFormat`
        :param exportFormat: The format of the file.
        :rtype: :class:`bool`
        :return: :class:`True` if succeeded, :class:`False` otherwise.
        """
        raise NotImplementedError()
    
    def openFile(self, path, openFormat):
        """
        Import a list of entries from a BibTeX file in a given format and overwrites all existing entries.
        :type path: :class:`str`
        :param path: The path to a file.
        :type openFormat: :class:`utils.settings.ImportFormat`
        :param openFormat: The format of the file.
        :rtype: :class:`bool`
        :return: :class:`True` if succeeded, :class:`False` otherwise.
        """
        raise NotImplementedError()
    
    def addEntry(self, entryBibTeX, entryType = None):
        """
        Add a new entry. If :class:`entryBibTeX==Empty Entry`, an empty entry is created.
        :type entryBibTeX: :class:`str`
        :param entryBibTeX: The BibTeX reference of the entry. 
        :rtype: :class:`int`
        :return: The I{id} of the new entry. ``None`` is returned if failed.
        """
        raise NotImplementedError()
    
    def duplicateEntry(self, entryId):
        """
        Create a copy of an existing entry.
        :type entryId: :class:`int`
        :param entryId: The I{id} of the entry to copy.
        :rtype: :class:`int`
        :return: The I{id} of the new entry. ``None`` is returned if failed.
        """
        raise NotImplementedError()
    
    def updateEntry(self, entryId, entryBibTeX):
        """
        Update an entry with a new BibTeX reference.
        :type entryId: :class:`int`
        :param entryId: The I{id} of the entry to update. 
        :type entryBibTeX: :class:`str`
        :param entryBibTeX: The BibTeX reference. 
        :rtype: :class:`bool`
        :return: :class:`True` if succeeded, :class:`False` otherwise.
        """
        raise NotImplementedError()
    
    def updateEntryField(self, entryId, fieldName, fieldValue):
        """
        Update an entry BibTeX reference field with a new value.
        
        :type entryId: :class:`int`
        :param entryId: The I{id} of the entry to update. 
        :type fieldName: :class:`str`
        :param fieldName: The field name.
        :type fieldValue: :class:`str`
        :param fieldValue: The field value.
        :rtype: :class:`bool`
        :return: :class:`True` if succeeded, :class:`False` otherwise.
        """
        raise NotImplementedError()
    
    def deleteEntry(self, entryId):
        """
        Delete an entry.
        :type entryId: :class:`int`
        :param entryId: The I{id} of the entry to delete. 
        :rtype: :class:`bool`
        :return: :class:`True` if succeeded, :class:`False` otherwise.
        """
        raise NotImplementedError()
    
    def previewEntry(self, entryId):
        """
        Convert an entry into its HTML representation following the bibliography style specified in :class:`utils.settings.Preferences`.
        :type entryId: :class:`int`
        :param entryId: The I{id} of the entry to preview. 
        :rtype: :class:`str`
        :return: The HTML representation of the entry.
        :raises: Exception: If entry not found.
        """
        raise NotImplementedError()
        
    def generateAllKeys(self):
        """
        Generate the key of all entries.
        :rtype: :class:`bool`
        :return: :class:`True` if all keys were generated successfully, :class:`False` otherwise.
        """
        raise NotImplementedError()
        
    def validateAllEntries(self):
        """
        Validate all entries.
        """
        raise NotImplementedError()
    
    def undo(self):
        """
        Undo the last action performed. 
        :rtype: :class:`bool`
        :return: :class:`True` if succeeded, :class:`False` otherwise.
        """
        raise NotImplementedError()
    
    def hasUndoableActionLeft(self):
        """
        Verify if there is any action to undo.
        :rtype: :class:`bool`
        :return: :class:`True` if succeeded, :class:`False` otherwise.
        """
        raise NotImplementedError()
    
    def getEntryPaperURL(self, entryId):
        """
        Get the URL of the paper of the selected entry.
        :type entryId: :class:`int`
        :param entryId: The I{id} of the entry. 
        :rtype: :class:`str`
        :return: The URL (or path) to the file.
        :raises: Exception: If entry not found.
        """
        raise NotImplementedError()
    
    def search(self, query):
        """
        Search for entries that satisfy the query provided.
        :type query: :class:`str`
        :param query: The query to match.
        :rtype: :class:`int`
        :return: Number of matches if search succeeded, negative number otherwise.
        """
        raise NotImplementedError()
    
    def sort(self, field, reverse=False):
        """
        Inplace sort of in alphabetically increasing order all entries with respect to a field.
        :type field: :class:`EntryListColumn`
        :param field: The field to sort on.
        :type field: :class:`bool`
        :param reverse: Sort in decreasing order when :class:`True`.
        :rtype: :class:`bool`
        :return: :class:`True` if succeeded, :class:`False` otherwise.
        """
        raise NotImplementedError()

    def getEntry(self, entryId):
        """
        Convert an entry into an :class:`EntryDict`.
        :type entryId: :class:`int`
        :param entryId: The I{id} of the entry. 
        :rtype: :class:`list` of :class:`EntryDict`
        :return: The entry.
        :raises: Exception: If entry not found.
        """
        raise NotImplementedError()

    def getBibTeX(self, entryId):
        """
        Convert an entry into its BibTeX reference.
        :type entryId: :class:`int`
        :param entryId: The I{id} of the entry. 
        :rtype: :class:`str`
        :return: The BibTeX reference.
        :raises: Exception: If entry not found.
        """
        raise NotImplementedError()
    
    def getEntryRequiredFields(self, entryId):
        """
        Get the required fields of an entry.
        
        :type entryId: :class:`int`
        :param entryId: The I{id} of the entry. 
        :rtype: :class:`dict`
        :return: The dictionary of required fields.
        :raises: Exception: If entry not found.
        """
        raise NotImplementedError()
    
    def getEntryOptionalFields(self,entryId):
        """
        Get the optional fields of an entry.
        
        :type entryId: :class:`int`
        :param entryId: The I{id} of the entry. 
        :rtype: :class:`dict`
        :return: The dictionary of optional fields.
        :raises: Exception: If entry not found.
        """
        raise NotImplementedError()
    
    def getEntryAdditionalFields(self,entryId):
        """
        Get the additional fields of an entry.
        
        :type entryId: :class:`int`
        :param entryId: The I{id} of the entry. 
        :rtype: :class:`dict`
        :return: The dictionary of additional fields.
        :raises: Exception: If entry not found.
        """
        raise NotImplementedError()
    
    def getAllEntries(self):
        """
        Get the list of all entries.
        :rtype: :class:`list` of :class:`EntryDict`
        :return: The list of entries.
        """
        raise NotImplementedError()
    
    def getEntryCount(self):
        """
        Get the total number of entries.
        :rtype: :class:`int`
        :return: The total.
        """
        raise NotImplementedError()
    
    def getSearchResult(self):
        """
        Get the list of entries filtered by the search.
        :rtype: :class:`list` of :class:`EntryDict`
        :return: The list of entries.
        """
        raise NotImplementedError()
    
    def getSearchResultCount(self):
        """
        Get the total number of results from the search.
        :rtype: :class:`int`
        :return: The total.
        """
        raise NotImplementedError()
        
    def iterAllEntries(self):
        """
        Iterator over the list of all entries.
        :rtype: ``generator`` of :class:`EntryDict`
        :return: The list of entries.
        """
        raise NotImplementedError()
        
    def iterSearchResult(self):
        """
        Get the list of entries filtered by the search.
        :rtype: ``generator`` of :class:`EntryDict`
        :return: The list of entries.
        """
        raise NotImplementedError()
