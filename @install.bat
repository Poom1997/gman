@echo off
echo Installing Program & echo Please wait a few minutes
pip install bcrypt
pip install psycopg2
set VS100COMNTOOLS=%VS140COMNTOOLS%
pip install -U PySide==1.2.2

