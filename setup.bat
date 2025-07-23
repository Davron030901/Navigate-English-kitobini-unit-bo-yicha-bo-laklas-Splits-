@echo off
echo ==========================================
echo   PDF Unit Bo'lish Dasturi O'rnatish
echo ==========================================
echo.

REM Python mavjudligini tekshirish
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python topilmadi!
    echo Python 3.7+ ni o'rnatib, PATH ga qo'shing.
    pause
    exit /b 1
)

echo ✅ Python topildi
python --version

REM Virtual environment yaratish
if not exist "env" (
    echo.
    echo 📦 Virtual environment yaratilmoqda...
    python -m venv env
) else (
    echo ✅ Virtual environment mavjud
)

REM Virtual environment ni aktivlashtirish
echo.
echo 🔄 Virtual environment aktivlashtirilmoqda...
call env\Scripts\activate.bat

REM pip ni yangilash
echo.
echo 🔄 pip yangilanmoqda...
python -m pip install --upgrade pip

REM Dependencylarni o'rnatish
echo.
echo 📥 Dependencylar o'rnatilmoqda...
pip install -r requirements.txt

REM Muvaffaqiyat xabari
echo.
echo ==========================================
echo ✅ O'rnatish muvaffaqiyatli yakunlandi!
echo ==========================================
echo.
echo Keyingi qadamlar:
echo 1. coursebook.pdf va workbook.pdf fayllarini bu papkaga qo'ying
echo 2. run_server.bat ni ishga tushiring web interfeys uchun
echo 3. Yoki python main.py ni ishga tushiring terminal uchun
echo.

REM Virtual environment ni deaktivlashtirish
deactivate

pause
