@echo off
echo Pushing to GitHub...

REM Get the commit message from command line argument
set msg=%1
if "%msg%"=="" set msg="Update"

REM Add all changes
git add .

REM Commit with message
git commit -m "%msg%"

REM Push to main branch
git push origin main

echo Done!
pause
