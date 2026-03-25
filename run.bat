@echo off

cd /d %~dp0

mkdir logs
mkdir reports
mkdir screenshots

pytest -s -v

pause