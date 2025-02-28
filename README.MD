# 🎤 YouTube Audio Transcriber  

Este script permite descargar el audio de un video de **YouTube** y transcribirlo usando **OpenAI Whisper**.  

## 🚀 Características  
👉 Descarga automáticamente el audio de un video de YouTube.  
👉 Convierte el audio a formato WAV.  
👉 Usa **Whisper** para transcribir el contenido del audio.  
👉 Guarda la transcripción en un archivo de texto.  
👉 Soporta ejecución con **argumentos** o **modo interactivo**.  

## 🛠️ Instalación y Configuración  

### **1️⃣ Clonar el repositorio**  
```bash  
git clone https://github.com/TU_USUARIO/youtube_transcriber.git  
cd youtube_transcriber  
```  

### **2️⃣ Instalar dependencias**  
Asegúrate de tener **Python 3.8+** instalado y ejecuta:  
```bash  
pip install -r requirements.txt  
```  

### **3️⃣ Instalar FFmpeg (si no lo tienes)**  
- **Windows:** Descarga desde [FFmpeg.org](https://ffmpeg.org/download.html) y agrégalo a `PATH`.  
- **Linux:**  
  ```bash  
  sudo apt update && sudo apt install ffmpeg  
  ```  
- **MacOS:**  
  ```bash  
  brew install ffmpeg  
  ```  

## 🎯 Uso del Script  

### **1️⃣ Modo interactivo (sin argumentos)**  
Ejecuta el script y pega la URL del video cuando se solicite:  
```bash  
python transcriber.py  
```  

### **2️⃣ Modo automático (con URL como argumento)**  
Pasa la URL del video directamente al ejecutar el script:  
```bash  
python transcriber.py "https://www.youtube.com/watch?v=VIDEO_ID"  
```  

### **3️⃣ Ubicación del archivo de salida**  
El texto transcrito se guardará en:  
```
output/transcription.txt  
```  

## ⚙️ Opcional: Actualizar dependencias  
Si en el futuro necesitas actualizar las dependencias, usa:  
```bash  
pip freeze > requirements.txt  
```  

## 🛠️ Contribución y Desarrollo  
1. **Haz un fork** del repositorio.  
2. Crea una nueva rama:  
   ```bash  
   git checkout -b mi-nueva-rama  
   ```  
3. Realiza cambios y confirma:  
   ```bash  
   git commit -m "Agregada nueva funcionalidad"  
   ```  
4. Sube los cambios y crea un **Pull Request**.  

## 📚 Licencia  
Este proyecto se distribuye bajo la **Licencia MIT**.

