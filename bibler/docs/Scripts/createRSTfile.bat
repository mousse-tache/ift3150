::cd "C:\<path to working directory>\docs\Scripts"

SET /p package="Give the name of the package and press <ENTER>... "
SET /p module="Give the name of the module and press <ENTER>... "
SET /p file="Give the name of the FILE.PY and press <ENTER>... "

CreateRSTfile.py %package% %module% %file%

move /-y .\*.rst ..\source

:END
pause