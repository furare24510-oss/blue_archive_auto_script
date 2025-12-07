@echo off
REM BAAS GUI 実行スクリプト
REM このファイルをダブルクリックして BAAS GUI を起動します

cd /d "%~dp0"
call venv\Scripts\activate.bat
python window.py
pause
