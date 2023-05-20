# Utilisez une image de base Python
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY app.py /app
COPY requirements.txt /app

# Installer les dépendances spécifiées dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port utilisé par l'application Dash
EXPOSE 8050

# Définir la commande d'exécution de l'application
CMD ["python", "app.py"]

