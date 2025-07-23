@echo off
echo ==========================================
echo   PDF Unit Bo'lish Dasturi Web Server
echo ==========================================
echo.

REM Virtual environment ni aktivlashtirish
if exist "env\Scripts\activate.bat" (
    echo Virtual environment topildi, aktivlashtirilmoqda...
    call env\Scripts\activate.bat
) else (
    echo Virtual environment topilmadi!
    echo Avval setup.bat ni ishga tushiring.
    pause
    exit /b 1
)

REM Server ni ishga tushirish
echo.
echo Server ishga tushirilmoqda...
echo Sayt: http://localhost:5000
echo Serverni to'xtatish uchun Ctrl+C ni bosing
echo.

python server.py

REM Virtual environment ni deaktivlashtirish
deactivate

echo.
echo Server to'xtatildi.
pause
