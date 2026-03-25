@echo off

cd /d %~dp0

pytest -s -v

pause