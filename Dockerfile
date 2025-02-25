# Usamos Python 3.9 como base
FROM python:3.9

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos primero el archivo de dependencias para aprovechar la caché de Docker
COPY requirements.txt /app/

# Actualizamos pip e instalamos las dependencias
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente al contenedor
COPY . /app

# Exponemos el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
