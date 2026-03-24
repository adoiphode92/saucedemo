@echo off

cd /d %~dp0

call .venv\Scripts\activate

pytest -s -v --html=reports\report.html --browser chrome

pause