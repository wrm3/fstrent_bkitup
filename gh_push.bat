@echo off
echo GitHub Push Utility

REM Get the bump type and commit message
set /p BUMP_TYPE="Enter bump type (major/minor/patch) or none: "
set /p MESSAGE="Enter commit message: "

REM Add all changes and commit first
git add .
git commit -m "%MESSAGE%"

REM If bump type is specified, do version bump
if not "%BUMP_TYPE%"=="none" (
    echo Bumping %BUMP_TYPE% version...
    python -m bumpversion --allow-dirty %BUMP_TYPE%
)

REM Push to main branch with tags
git push origin main --tags

echo Done!
pause
