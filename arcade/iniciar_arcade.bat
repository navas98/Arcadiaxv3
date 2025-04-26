@echo off
cd /d "C:\Users\Diana\Desktop\Arcadiaxv3\arcade"

:: Obtener IP local (en español usa "Dirección IPv4")
for /f "tokens=14" %%i in ('ipconfig ^| findstr /c:"Dirección IPv4"') do set IP_LOCAL=%%i

echo IP detectada: %IP_LOCAL%

:: Modificar línea IP= en el archivo .env sin borrar otras variables
powershell -Command ^
    "(Get-Content .env) -replace '^IP=.*', 'IP=%IP_LOCAL%' | Set-Content .env"

:: Iniciar sistema
echo Iniciando sistema arcade...
python sistema.py

pause
