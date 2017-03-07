Search.setIndex({envversion:50,filenames:["AddCommand","Article","Author","BiBlerApp","BibTeXExporter","BibTeXImporter","BibTeXParser","BibTeXParserWithNonStdFields","BibTeXParserWithStdFields","Book","Booklet","CSVExporter","CSVImporter","CommandClass","CommandExecutor","Conference","Contributor","ContributorField","DOI","DeleteCommand","DuplicateCommand","Editor","EmptyEntry","EndNoteImporter","EntryClass","EntryIdGenerator","ExportCommand","Exporter","FieldClass","FieldName","FieldNameClass","FieldNames","FieldValueMappingToHTML","FieldValueMappingToSimple","GenerateAllKeysCommand","HTMLExporter","ImpExClass","ImportCommand","Importer","Inbook","Incollection","Inproceedings","Manual","Mastersthesis","Misc","MySQLExporter","OpenCommand","Organization","Pages","Paper","Phdthesis","PreviewCommand","Proceedings","ReferenceManager","SearchCommand","SortCommand","Techreport","UndoCommand","UndoableCommand","Unpublished","UpdateCommand","ValidateAllCommand","ValidationResult","Year","app","bibclass","bibler","bibtex_parser","command","entry","field","gui","impex","index","manager","userInterface","utils"],objects:{"":{__init__:[66,0,0,"-"],app:[64,0,0,"-"],gui:[71,0,0,"-"],utils:[76,0,0,"-"]},"__init__.BiBler":{__init__:[65,2,1,""],start:[65,2,1,""],startGUI:[65,2,1,""]},"app.bibtex_parser":{BibTeXParser:[6,1,1,""],BibTeXParserWithNonStdFields:[7,1,1,""],BibTeXParserWithStdFields:[8,1,1,""]},"app.bibtex_parser.BibTeXParser":{__init__:[6,2,1,""],parse:[6,2,1,""]},"app.bibtex_parser.BibTeXParserWithNonStdFields":{__init__:[7,2,1,""],parseFields:[7,2,1,""]},"app.bibtex_parser.BibTeXParserWithStdFields":{_BibTeXParserWithStdFields__parseNested:[8,2,1,""],_BibTeXParserWithStdFields__unicodeToTex:[8,2,1,""],__init__:[8,2,1,""],findField:[8,2,1,""],parse:[8,2,1,""],parseEntryHeader:[8,2,1,""],parseFields:[8,2,1,""]},"app.command":{AddCommand:[0,1,1,""],Command:[13,1,1,""],CommandExecutor:[14,1,1,""],DeleteCommand:[19,1,1,""],DuplicateCommand:[20,1,1,""],ExportCommand:[26,1,1,""],GenerateAllKeysCommand:[34,1,1,""],ImportCommand:[37,1,1,""],OpenCommand:[46,1,1,""],PreviewCommand:[51,1,1,""],SearchCommand:[54,1,1,""],SortCommand:[55,1,1,""],UndoCommand:[57,1,1,""],UndoableCommand:[58,1,1,""],UpdateCommand:[60,1,1,""],ValidateAllCommand:[61,1,1,""]},"app.command.AddCommand":{__init__:[0,2,1,""],execute:[0,2,1,""],unexecute:[0,2,1,""]},"app.command.Command":{__init__:[13,2,1,""]},"app.command.CommandExecutor":{__init__:[14,2,1,""],canUndo:[14,2,1,""],execute:[14,2,1,""],undo:[14,2,1,""]},"app.command.DeleteCommand":{__init__:[19,2,1,""],execute:[19,2,1,""],unexecute:[19,2,1,""]},"app.command.DuplicateCommand":{__init__:[20,2,1,""],execute:[20,2,1,""],unexecute:[20,2,1,""]},"app.command.ExportCommand":{__init__:[26,2,1,""],execute:[26,2,1,""]},"app.command.GenerateAllKeysCommand":{__init__:[34,2,1,""],execute:[34,2,1,""]},"app.command.ImportCommand":{__init__:[37,2,1,""],execute:[37,2,1,""],unexecute:[37,2,1,""]},"app.command.OpenCommand":{__init__:[46,2,1,""],execute:[46,2,1,""],unexecute:[46,2,1,""]},"app.command.PreviewCommand":{__init__:[51,2,1,""],execute:[51,2,1,""]},"app.command.SearchCommand":{__init__:[54,2,1,""],execute:[54,2,1,""]},"app.command.SortCommand":{__init__:[55,2,1,""],execute:[55,2,1,""],unexecute:[55,2,1,""]},"app.command.UndoCommand":{__init__:[57,2,1,""],execute:[57,2,1,""]},"app.command.UndoableCommand":{__init__:[58,2,1,""]},"app.command.UpdateCommand":{__init__:[60,2,1,""],execute:[60,2,1,""],unexecute:[60,2,1,""]},"app.command.ValidateAllCommand":{__init__:[61,2,1,""],execute:[61,2,1,""]},"app.entry":{Article:[1,1,1,""],Book:[9,1,1,""],Booklet:[10,1,1,""],Conference:[15,1,1,""],EmptyEntry:[22,1,1,""],Entry:[24,1,1,""],EntryIdGenerator:[25,1,1,""],Inbook:[39,1,1,""],Incollection:[40,1,1,""],Inproceedings:[41,1,1,""],Manual:[42,1,1,""],Mastersthesis:[43,1,1,""],Misc:[44,1,1,""],Phdthesis:[50,1,1,""],Proceedings:[52,1,1,""],Techreport:[56,1,1,""],Unpublished:[59,1,1,""],ValidationResult:[62,1,1,""]},"app.entry.Article":{__init__:[1,2,1,""],getContributors:[1,2,1,""],getEntryType:[1,3,1,""],toHtmlACM:[1,2,1,""],toHtmlDefault:[1,2,1,""]},"app.entry.Book":{__init__:[9,2,1,""],generateKey:[9,2,1,""],getContributors:[9,2,1,""],getEntryType:[9,3,1,""],toHtmlACM:[9,2,1,""],toHtmlDefault:[9,2,1,""],validate:[9,2,1,""]},"app.entry.Booklet":{__init__:[10,2,1,""],getContributors:[10,2,1,""],getEntryType:[10,3,1,""],toHtmlACM:[10,2,1,""],toHtmlDefault:[10,2,1,""]},"app.entry.Conference":{__init__:[15,2,1,""],getEntryType:[15,3,1,""]},"app.entry.EmptyEntry":{__init__:[22,2,1,""],generateKey:[22,2,1,""],getEntryType:[22,3,1,""],toBibTeX:[22,2,1,""],toCompleteHtmlACM:[22,2,1,""],toCompleteHtmlDefault:[22,2,1,""],validate:[22,2,1,""]},"app.entry.Entry":{_Entry__iterAllFieldsUnsorted:[24,2,1,""],_Entry__toHtml:[24,2,1,""],__init__:[24,2,1,""],formatField:[24,2,1,""],generateId:[24,2,1,""],generateKey:[24,2,1,""],getContributors:[24,2,1,""],getEntryType:[24,3,1,""],getField:[24,2,1,""],getFieldValue:[24,2,1,""],getId:[24,2,1,""],getKey:[24,2,1,""],iterAdditionalFields:[24,2,1,""],iterAllFields:[24,2,1,""],iterOptionalFields:[24,2,1,""],iterRequiredFields:[24,2,1,""],matchesExact:[24,2,1,""],matchesRegex:[24,2,1,""],setField:[24,2,1,""],setId:[24,2,1,""],setKey:[24,2,1,""],toBibTeX:[24,2,1,""],toCSV:[24,2,1,""],toCompleteHtmlACM:[24,2,1,""],toCompleteHtmlDefault:[24,2,1,""],toEntryDict:[24,2,1,""],toHtmlACM:[24,2,1,""],toHtmlDefault:[24,2,1,""],toSQL:[24,2,1,""],validate:[24,2,1,""]},"app.entry.EntryIdGenerator":{__init__:[25,2,1,""],getLastId:[25,2,1,""],getNewId:[25,2,1,""],instance:[25,4,1,""],reset:[25,2,1,""]},"app.entry.Inbook":{__init__:[39,2,1,""],getContributors:[39,2,1,""],getEntryType:[39,3,1,""],toHtmlACM:[39,2,1,""],toHtmlDefault:[39,2,1,""],validate:[39,2,1,""]},"app.entry.Incollection":{__init__:[40,2,1,""],getContributors:[40,2,1,""],getEntryType:[40,3,1,""],toHtmlACM:[40,2,1,""],toHtmlDefault:[40,2,1,""],validate:[40,2,1,""]},"app.entry.Inproceedings":{__init__:[41,2,1,""],getContributors:[41,2,1,""],getEntryType:[41,3,1,""],toHtmlACM:[41,2,1,""],toHtmlDefault:[41,2,1,""]},"app.entry.Manual":{__init__:[42,2,1,""],generateKey:[42,2,1,""],getContributors:[42,2,1,""],getEntryType:[42,3,1,""],toHtmlACM:[42,2,1,""],toHtmlDefault:[42,2,1,""],validate:[42,2,1,""]},"app.entry.Mastersthesis":{__init__:[43,2,1,""],getEntryType:[43,3,1,""]},"app.entry.Misc":{__init__:[44,2,1,""],getContributors:[44,2,1,""],getEntryType:[44,3,1,""],toHtmlACM:[44,2,1,""],toHtmlDefault:[44,2,1,""]},"app.entry.Phdthesis":{__init__:[50,2,1,""],getContributors:[50,2,1,""],getEntryType:[50,3,1,""],toHtmlACM:[50,2,1,""],toHtmlDefault:[50,2,1,""]},"app.entry.Proceedings":{__init__:[52,2,1,""],generateKey:[52,2,1,""],getContributors:[52,2,1,""],getEntryType:[52,3,1,""],toHtmlACM:[52,2,1,""],toHtmlDefault:[52,2,1,""]},"app.entry.Techreport":{__init__:[56,2,1,""],getContributors:[56,2,1,""],getEntryType:[56,3,1,""],toHtmlACM:[56,2,1,""],toHtmlDefault:[56,2,1,""]},"app.entry.Unpublished":{__init__:[59,2,1,""],getContributors:[59,2,1,""],getEntryType:[59,3,1,""],toHtmlACM:[59,2,1,""],toHtmlDefault:[59,2,1,""]},"app.entry.ValidationResult":{ERROR:[62,4,1,""],SUCCESS:[62,4,1,""],WARNING:[62,4,1,""],__init__:[62,2,1,""],getMessage:[62,2,1,""],getValue:[62,2,1,""],isValid:[62,2,1,""]},"app.field":{Author:[2,1,1,""],Contributor:[16,1,1,""],ContributorField:[17,1,1,""],DOI:[18,1,1,""],Editor:[21,1,1,""],Field:[28,1,1,""],FieldValueMappingToHTML:[32,1,1,""],FieldValueMappingToSimple:[33,1,1,""],Organization:[47,1,1,""],Pages:[48,1,1,""],Paper:[49,1,1,""],Year:[63,1,1,""]},"app.field.Author":{__init__:[2,2,1,""]},"app.field.Contributor":{__init__:[16,2,1,""]},"app.field.ContributorField":{ET_AL:[17,4,1,""],SPLIT:[17,4,1,""],__init__:[17,2,1,""],format:[17,2,1,""],getACMValue:[17,2,1,""],getContributors:[17,2,1,""],getContributorsCount:[17,2,1,""],getFirstLastName:[17,2,1,""],getFirstNameFirst:[17,2,1,""],getFirstNameLast:[17,2,1,""],getHTMLValue:[17,2,1,""],getHtmlDefaultValue:[17,2,1,""]},"app.field.DOI":{__init__:[18,2,1,""],format:[18,2,1,""]},"app.field.Editor":{__init__:[21,2,1,""]},"app.field.Field":{_Field__clean:[28,3,1,""],__init__:[28,2,1,""],format:[28,2,1,""],getACMValue:[28,2,1,""],getHTMLValue:[28,2,1,""],getHtmlDefaultValue:[28,2,1,""],getName:[28,2,1,""],getValue:[28,2,1,""],isEmpty:[28,2,1,""],setValue:[28,2,1,""],simplify:[28,3,1,""],toHTML:[28,3,1,""]},"app.field.FieldValueMappingToHTML":{__init__:[32,2,1,""],instance:[32,4,1,""]},"app.field.FieldValueMappingToSimple":{__init__:[33,2,1,""],instance:[33,4,1,""]},"app.field.Organization":{__init__:[47,2,1,""],getFirstWord:[47,2,1,""]},"app.field.Pages":{__init__:[48,2,1,""],format:[48,2,1,""]},"app.field.Paper":{__init__:[49,2,1,""]},"app.field.Year":{__init__:[63,2,1,""],getYear:[63,2,1,""]},"app.field_name":{FieldName:[30,1,1,""]},"app.field_name.FieldName":{Address:[30,4,1,""],Annote:[30,4,1,""],Author:[30,4,1,""],BookTitle:[30,4,1,""],Chapter:[30,4,1,""],Comment:[30,4,1,""],Crossref:[30,4,1,""],DOI:[30,4,1,""],Edition:[30,4,1,""],Editor:[30,4,1,""],Howpublished:[30,4,1,""],Institution:[30,4,1,""],Journal:[30,4,1,""],Key:[30,4,1,""],Month:[30,4,1,""],Note:[30,4,1,""],Number:[30,4,1,""],Organization:[30,4,1,""],Pages:[30,4,1,""],Paper:[30,4,1,""],Publisher:[30,4,1,""],School:[30,4,1,""],Series:[30,4,1,""],Title:[30,4,1,""],Type:[30,4,1,""],Volume:[30,4,1,""],Year:[30,4,1,""],_FieldName__all_names:[30,4,1,""],fromEntryListColumn:[30,3,1,""],getAllFieldNames:[30,3,1,""],iterAllFieldNames:[30,3,1,""],toEntryListColumn:[30,3,1,""]},"app.impex":{BibTeXExporter:[4,1,1,""],BibTeXImporter:[5,1,1,""],CSVExporter:[11,1,1,""],CSVImporter:[12,1,1,""],EndNoteImporter:[23,1,1,""],Exporter:[27,1,1,""],HTMLExporter:[35,1,1,""],ImpEx:[36,1,1,""],Importer:[38,1,1,""],MySQLExporter:[45,1,1,""]},"app.impex.BibTeXExporter":{__init__:[4,2,1,""],_exportEntry:[4,2,1,""]},"app.impex.BibTeXImporter":{__init__:[5,2,1,""],add:[5,2,1,""],importFile:[5,2,1,""]},"app.impex.CSVExporter":{__init__:[11,2,1,""],_exportEntry:[11,2,1,""],_preprocess:[11,2,1,""]},"app.impex.CSVImporter":{__init__:[12,2,1,""],importFile:[12,2,1,""]},"app.impex.EndNoteImporter":{_EndNoteImporter__cleanEndNoteEntry:[23,2,1,""],__init__:[23,2,1,""],add:[23,2,1,""],importFile:[23,2,1,""]},"app.impex.Exporter":{"export":[27,2,1,""],__init__:[27,2,1,""],_exportEntry:[27,2,1,""],_postprocess:[27,2,1,""],_preprocess:[27,2,1,""]},"app.impex.HTMLExporter":{__init__:[35,2,1,""],_exportEntry:[35,2,1,""],_postprocess:[35,2,1,""],_preprocess:[35,2,1,""]},"app.impex.ImpEx":{__init__:[36,2,1,""],closeDB:[36,2,1,""],openDB:[36,2,1,""]},"app.impex.Importer":{__init__:[38,2,1,""],importFile:[38,2,1,""]},"app.impex.MySQLExporter":{"export":[45,2,1,""],__init__:[45,2,1,""],_exportEntry:[45,2,1,""],_preprocess:[45,2,1,""],exportAssignments:[45,2,1,""],exportAuthors:[45,2,1,""],exportPapers:[45,2,1,""]},"app.manager":{ReferenceManager:[53,1,1,""]},"app.manager.ReferenceManager":{"delete":[53,2,1,""],_ReferenceManager__parseEntry:[53,2,1,""],_ReferenceManager__setKey:[53,2,1,""],__init__:[53,2,1,""],add:[53,2,1,""],deleteAll:[53,2,1,""],duplicate:[53,2,1,""],generateAllKeys:[53,2,1,""],getEntry:[53,2,1,""],getEntryCount:[53,2,1,""],getIndex:[53,2,1,""],getSearchResultCount:[53,2,1,""],insertAt:[53,2,1,""],iterEntries:[53,2,1,""],iterSearchResult:[53,2,1,""],search:[53,2,1,""],sort:[53,2,1,""],update:[53,2,1,""]},"app.user_interface":{BiBlerApp:[3,1,1,""]},"app.user_interface.BiBlerApp":{__init__:[3,2,1,""],addEntry:[3,2,1,""],deleteEntry:[3,2,1,""],duplicateEntry:[3,2,1,""],exit:[3,2,1,""],exportFile:[3,2,1,""],formatBibTeX:[3,3,1,""],generateAllKeys:[3,2,1,""],getAllEntries:[3,2,1,""],getBibTeX:[3,2,1,""],getContributors:[3,2,1,""],getEntry:[3,2,1,""],getEntryCount:[3,2,1,""],getEntryPaperURL:[3,2,1,""],getSearchResult:[3,2,1,""],getSearchResultCount:[3,2,1,""],hasUndoableActionLeft:[3,2,1,""],importFile:[3,2,1,""],iterAllEntries:[3,2,1,""],iterSearchResult:[3,2,1,""],openFile:[3,2,1,""],previewEntry:[3,2,1,""],search:[3,2,1,""],sort:[3,2,1,""],start:[3,2,1,""],undo:[3,2,1,""],updateEntry:[3,2,1,""],validateAllEntries:[3,2,1,""]},__init__:{BiBler:[65,1,1,""],FieldNames:[31,1,1,""]},app:{bibtex_parser:[67,0,0,"-"],command:[68,0,0,"-"],entry:[69,0,0,"-"],field:[70,0,0,"-"],field_name:[29,0,0,"-"],impex:[72,0,0,"-"],manager:[74,0,0,"-"],user_interface:[75,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","staticmethod","Python static method"],"4":["py","attribute","Python attribute"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:staticmethod","4":"py:attribute"},terms:{"abstract":[24,36],"default":[8,17,24,28,35,66],"enum":30,"export":[4,5,11,12,23,27,35,36,45,72],"function":[3,36],"import":[5,12,23],"int":[3,4,5,11,12,17,23,24,27,35,45,53],"new":[6,29,64,66,67,68,69,70,71,72,74,75,76],"public":53,"return":[3,4,5,8,11,12,17,23,24,27,28,30,35,45,47,53,62,63],"static":[1,3,9,10,15,22,24,28,30,39,40,41,42,43,44,50,52,56,59],"true":[24,28],__init__:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65],_bibtexparserwithstdfields__parsenest:8,_bibtexparserwithstdfields__unicodetotex:8,_endnoteimporter__cleanendnoteentri:23,_entry__iterallfieldsunsort:24,_entry__tohtml:24,_exportentri:[4,11,27,35,45],_field__clean:28,_fieldname__all_nam:30,_id:24,_postprocess:[27,35],_preprocess:[11,27,35,45],_referencemanager__parseentri:53,_referencemanager__setkei:53,aaa:28,accept:6,access:66,accord:[3,28],acm:[17,24,28],add:[5,23,53,66],addentri:[3,53],addit:[7,24,30],additionalfield:24,address:30,all:[3,7,8,24,28,30,31,53,68],allow:7,alphabet:30,also:66,alwai:[3,24],ani:[24,28,44],annot:30,annote:30,any:36,api:[66,75],app:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63],app_interfac:[3,24,30,31,66],applic:[3,64,65,66,75],arg:[32,33],ase:16,assign:[24,45],assum:66,avail:[24,25],back:25,base:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63],befor:16,behavior:64,bibler:[23,30],bibler_statechart:66,bibliograph:17,bibtex:[3,4,5,6,7,8,17,23,24,28],bibtex_pars:[6,7,8,64],bibtexpars:3,bibtexparserwithstdfield:7,bitex:67,booktitl:30,bool:[24,28,62],bound:10,can:[6,66],canundo:14,chang:66,chapter:[30,39],charact:[6,28],check:24,clean:28,close:[8,36,66],closedb:36,code:[5,23,24],column:[11,12,30],come:23,command:0,comment:30,compat:15,consist:[11,12],constructor:[0,6,7,8,13,14,19,20,26,34,37,46,51,54,55,57,58,60,61,65],contain:[30,64,68,71,76],contributor:3,contributorfield:2,control:71,convert:[24,28,30],core:64,correctli:[24,28],correspond:[8,30],could:3,creat:[29,64,66,67,68,69,70,71,72,74,75,76],croix:16,crossref:30,csv:[11,12],data:23,databas:[36,45],def:17,defin:[17,24,64],delet:53,deleteal:53,deleteentri:[3,53],delimit:[6,8],deprec:15,design:68,dict:[32,33],dictionari:24,digit:63,doc:36,document:[42,44],doe:[24,28],duplic:[5,23,53],duplicateentri:[3,53],dure:[4,5,11,12,23,27,35,45],each:[11,12,70],eacut:28,edit:30,edition:30,editor:[3,16],empti:[24,28,66],emptyentri:8,encod:28,end:16,endnote:23,entri:[1,3,4,5,6,7,8,9,10,11,12,15,22,23,24,25,27,28,30,31,35,38,39,40,41,42,43,44,45,50,52,53,56,59,62,66],entry:[1,4,5,8,9,10,11,12,22,23],entrybibtex:[0,3,53,60],entrydict:24,entryid:[3,19,51,53,60],entrylistcolumn:[30,31],enumer:31,error:[4,5,11,12,23,27,35,45,62],et_al:17,etc:16,eugen:[16,29,64,66,67,68,69,70,71,72,74,75,76],even:8,everi:[24,28,36],exampl:28,exception:[3,4,5,11,12,17,23,24,27,35,45,53],execut:[0,14,19,20,26,34,37,46,51,54,55,57,60,61,66],exist:24,exit:[3,66],explicit:9,exportassign:45,exportauthor:45,exporter:[4,11],exportfil:3,exportformat:[3,26],exportpap:45,express:24,fals:[3,24,28,53,55],field1:[6,24],field2:[6,24],field:[2,3,6,7,8,11,12,16,17,18,21,23,24],field_nam:[30,31],file:[4,5,11,12,23,27,35,36,38,45,76],filter:53,find:[8,24],findfield:8,first:[11,12,16,17,47,53],firstnameord:17,florin:[29,64,66,67,68,69,70,71,72,74,75,76],follow:[17,24,28,35,66],form:49,format:[3,6,17,18,24,27,28,38,48],formatbibtex:3,formatfield:24,found:[3,53],four:63,from:[1,5,12,23,24,38,66],fromentrylistcolumn:30,gener:[24,25,28,30,53],generateallkei:[3,53],generateid:24,generatekei:[9,22,24,42,52],get:[3,17,24,25,28,30,47,49,53,63],getacmvalu:[17,28],getallentri:3,getallfieldnam:30,getbibtex:3,getcontributor:[1,3,9,10,17,24,39,40,41,42,44,50,52,56,59],getcontributorscount:17,getentri:[3,53],getentrycount:[3,53],getentrypaperurl:3,getentrytyp:[1,9,10,15,22,24,39,40,41,42,43,44,50,52,56,59],getfield:24,getfieldvalu:24,getfirstlastnam:17,getfirstnamefirst:17,getfirstnamelast:17,getfirstword:47,gethtmldefaultvalu:[17,28],gethtmlvalu:[17,28],getid:24,getindex:53,getkei:24,getlastid:25,getmessag:62,getnam:28,getnewid:25,getsearchresult:3,getsearchresultcount:[3,53],getvalu:[28,62],getyear:63,given:53,graphic:[66,71],gui:[3,24,30,31,65,66],handler:36,hasundoableactionleft:3,have:[28,40],head:65,hold:[5,12,23,38,53],howpublish:30,html:[17,24,28,35,36],http:[17,36],iapplicat:[3,66],ignor:[6,24],ignoreemptyfield:24,impex:[4,5,11,12,23,27,35],implement:[66,68],importantfield:24,importer:[5,12,23],importfil:[3,5,12,23,38],importformat:[3,37],includ:15,increment:25,index:[53,73],individu:17,initi:25,inplac:24,inproceed:[15,23],inproceedings:15,input:6,insert:[24,45],insertat:53,insid:8,instanc:[25,32,33],institut:[10,30,56,59],interact:66,interfac:[64,66,71,73],inv_separ:8,invalid:3,invers:12,invok:57,isempti:28,issu:25,isvalid:62,iteradditionalfield:24,iterallentri:3,iterallfield:24,iterallfieldnam:30,iterat:[24,30,53],iterentri:53,iteroptionalfield:24,iterrequiredfield:24,itersearchresult:[3,53],journal:[1,23,30],kei:[6,8,24,30,53],key:[6,24],king:16,kwarg:[32,33],last:[16,17,25,45,63],launcher:65,legal:17,less:65,level:8,librari:36,like:16,line:[6,66],list:[3,4,5,11,12,17,23,24,27,30,35,38,45,53],look:8,luther:16,magazin:1,mai:[39,66],main:[3,66],manag:[0,5,12,13,19,20,23,26,34,37,38,46,51,53,54,55,58,60,61,64,73],martin:16,master:43,match:24,matchesexact:24,matchesregex:24,meant:12,messag:62,miss:24,mode:36,month:30,more:53,msg:62,multilin:6,multipl:17,must:[12,17],mysql:45,name:[10,11,12,16,17,24,28,29,30,31,47],need:66,nest:[6,8],next:[24,25],non:7,none:[25,32,33,49,53],note:[3,30],nov:[29,64,66,67,68,69,70,71,72,74,75,76],number:[4,5,11,12,17,23,27,30,35,45,56,59],object:[6,8,13,14,16,24,25,28,30,36,53,62],occur:[4,5,11,12,23,27,35,45],oncica:[29,64,66,67,68,69,70,71,72,74,75,76],onli:8,open:[8,36],opendb:36,openfil:3,openformat:[3,46],openoffic:17,oper:[12,53],option:[6,24,62],optionalfield:24,order:[24,30],org:[17,36],organ:[3,30,47],organiz:30,originalentryid:20,other:[17,28,44,56,59],otherwis:[3,24,28],output:45,outsid:6,over:[24,30,53],own:40,packagetre:66,page:[30,39],paper:[30,45],param:[3,4,5,11,12,16,23,27,28,30,35,36,38,45,49,53],paramet:[6,7,8,24,62],pars:[3,6,7,8],parseentryhead:8,parsefield:[7,8],parser:67,part:[39,40,63],patch:23,path:[3,4,5,11,12,23,26,27,35,36,37,38,45,46],pattern:68,phdthesi:43,possibl:31,prefer:66,preposit:16,present:63,previewentri:3,print:10,proceed:[15,41],process:[4,5,11,12,23,27,35,45],programmat:66,provid:3,publish:[9,10,30,53,56,59],python:36,queri:[3,24,53,54],rais:[3,4,5,11,12,17,23,24,27,35,45,53],rang:39,refer:[5,12,23,24,38,53],referencemanag:[5,12,23,38],regular:24,remov:[5,23,28],render:71,report:[56,59],repres:[24,28,29,67,69,70,72,74,75],request:24,requir:24,requiredfield:24,reset:25,resourc:76,respons:6,result:[8,62],reusabl:76,revers:[3,53,55],row:[11,12,24],rtype:[3,4,5,11,12,17,23,27,28,30,35,45,47,53,63],same:[7,8,15,24,30],school:[30,56,59],scribe:15,script:45,search:[3,53,73],second:45,section:39,see:[3,28,53],separ:[8,17],sequenc:24,seri:[23,30,56,59],set:[24,28,53,66,76],setfield:24,setid:24,setkei:24,setvalu:28,shorthand:[5,23],simplifi:28,sometim:23,sort:[3,30,53],sourc:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65],space:6,special:28,specif:[36,38,66],specifi:[27,38],split:17,sponsor:10,sql:24,standard:[3,7,8,28,30],start:[3,65,66],startgui:65,statechart:66,statement:[24,45],still:24,str:[3,4,5,6,7,8,11,12,16,17,23,24,27,28,35,36,38,45,47,49,62,63],string:[3,6,7,8,23,28],strip:28,style:[17,24,28,35],stylewrit:24,substr:24,success:62,successfulli:[3,4,5,11,12,23,27,35,45],suffix:16,support:[3,6,17,36],syriani:[29,64,66,67,68,69,70,71,72,74,75,76],tab:[11,12],tabifi:24,tabl:45,technic:42,tertiari:23,than:53,thei:[3,63],thesi:[43,50],thi:[12,23,24,28,29,64,66,67,68,69,70,71,72,74,75,76],through:66,titl:[23,30,40],tobibtex:[22,24],tocompletehtmlacm:[22,24],tocompletehtmldefault:[22,24],tocsv:24,toentrydict:24,toentrylistcolumn:30,tohtml:28,tohtmlacm:[1,9,10,24,39,40,41,42,44,50,52,56,59],tohtmldefault:[1,9,10,24,39,40,41,42,44,50,52,56,59],tosql:24,total:[4,5,11,12,23,27,35,45],transform:8,two:31,type:[3,4,5,6,8,11,12,16,22,23,24,27,28,30,35,36,38,44,45,49,53,62],undo:[3,14],undoablecommand:[0,19,20,37,55],unexecut:[0,19,20,37,46,55,60],unicod:6,union:31,uniqu:[24,53],updat:53,updateentri:[3,53],url:53,user:[64,66,71,73],user_interfac:[3,53],usual:[24,56,59],util:[66,73],val:[6,62],valid:[9,22,24,30,39,40,42,62],validateallentri:3,valu:[2,6,8,17,18,21,24,25,28,47,48,49,62,63],value11:6,value12:6,value13:6,value1:[6,24],value2:[6,24],verfi:28,verifi:24,version:[29,64,66,67,68,69,70,71,72,74,75,76],volum:30,von:[16,17],want:66,warn:62,warning:62,well:30,whatev:39,when:23,whether:62,which:[39,49],within:[8,24,56,59],without:10,word:47,work:10,written:6,www:17,year:[30,53],you:66},titles:["Class AddCommand","Class Article","Class Author","Class BiBlerApp","Class BibTeXExporter","Class BibTeXImporter","Class BibTeXParser","Class BibTeXParserWithNonStdFields","Class BibTeXParserWithStdFields","Class Book","Class Booklet","Class CSVExporter","Class CSVImporter","Class Command","Class CommandExecutor","Class Conference","Class Contributor","Class ContributorField","Class DOI","Class DeleteCommand","Class DuplicateCommand","Class Editor","Class EmptyEntry","Class EndNoteImporter","Class Entry","Class EntryIdGenerator","Class ExportCommand","Class Exporter","Class Field","Module FieldName","Class FieldName","Class FieldNames","Class FieldValueMappingToHTML","Class FieldValueMappingToSimple","Class GenerateAllKeysCommand","Class HTMLExporter","Class ImpEx","Class ImportCommand","Class Importer","Class Inbook","Class Incollection","Class Inproceedings","Class Manual","Class Mastersthesis","Class Misc","Class MySQLExporter","Class OpenCommand","Class Organization","Class Pages","Class Paper","Class Phdthesis","Class PreviewCommand","Class Proceedings","Class ReferenceManager","Class SearchCommand","Class SortCommand","Class Techreport","Class UndoCommand","Class UndoableCommand","Class Unpublished","Class UpdateCommand","Class ValidateAllCommand","Class ValidationResult","Class Year","Package app","Class BiBler","Package BiBler","Module bibtex_parser","Module command","Module entry","Module Field","Package gui","Module Impex","Welcome to BiBler&#8217;s documentation!","Module Manager","Module User Interface","Package utils"],titleterms:{"class":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,68,69,70,72,74,75],"import":[29,67,68,69,70,72,74,75],addcommand:0,app:64,articl:1,author:2,bibler:[65,66,73],biblerapp:3,bibtex_pars:67,bibtexexport:4,bibteximport:5,bibtexpars:6,bibtexparserwithnonstdfield:7,bibtexparserwithstdfield:8,book:9,booklet:10,command:[13,68],commandexecutor:14,confer:15,content:73,contributor:16,contributorfield:17,csvexporter:11,csvimporter:12,deletecommand:19,document:73,doi:18,duplicatecommand:20,editor:21,emptyentri:22,endnoteimport:23,entri:69,entry:24,entryidgener:25,exportcommand:26,exporter:27,field:[28,70],fieldnam:[29,30,31],fieldvaluemappingtohtml:32,fieldvaluemappingtosimpl:33,generateallkeyscommand:34,gui:71,htmlexporter:35,impex:[36,72],importcommand:37,importer:38,inbook:39,incollect:40,indice:73,inproceed:41,interfac:75,manag:74,manual:42,mastersthesi:43,misc:44,modul:[29,67,68,69,70,72,74,75],mysqlexport:45,opencommand:46,organiz:47,packag:[64,66,71,76],page:48,paper:49,phdthesi:50,previewcommand:51,proceed:52,referencemanag:53,searchcommand:54,sortcommand:55,tabl:73,techreport:56,undoablecommand:58,undocommand:57,unpublish:59,updatecommand:60,user:75,util:76,validateallcommand:61,validationresult:62,welcom:73,year:63}})