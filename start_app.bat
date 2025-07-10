@echo off
echo ========================================
echo IBKR Data Collector - Starting Application
echo ========================================
echo.

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting Flask application...
echo.
echo The application will be available at:
echo http://localhost:5001
echo.
echo Press Ctrl+C to stop the application
echo.

python src\main.py

