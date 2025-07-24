@echo off
echo 📁 Navegando a la carpeta del proyecto...
cd /d "%~dp0"

echo 🔁 Creando entorno virtual...
python -m venv .venv

echo ✅ Activando entorno virtual...
call .venv\Scripts\activate

echo 📦 Instalando dependencias...
pip install -r requirements.txt

echo 🧼 Ejecutando pipeline completo...
python main.py

echo 🎉 Proceso completado.
pause
