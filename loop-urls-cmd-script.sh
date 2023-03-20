@echo off
setlocal enabledelayedexpansion
for /F "tokens=*" %%G in (urls.txt) do (
    set cmd=python script.py -u %%G --host asdf.com --workers 150
    set cmd=!cmd:url=%%G!
    echo Running command: !cmd!
    !cmd! > "output_%%G.txt"
)
