@echo off
cd /d "%~dp0"
set UV_PYTHON_INSTALL_DIR=%~dp0.python
set UV_CACHE_DIR=%~dp0.uv-cache
uv.exe run --frozen ocr.py
pause
