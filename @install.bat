@echo off
echo Installing Program & echo Please wait a few minutes
echo You need Python 3.X and above to run this file.
pip install bcrypt
pip install psycopg2
set VS100COMNTOOLS=%VS140COMNTOOLS%
pip install -U PySide==1.2.2
pip install pillow
pip install jinja2
cls
echo Program has been installed successfully
pause