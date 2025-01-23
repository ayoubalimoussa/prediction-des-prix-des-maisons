FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt /app
COPY predict.py /app
COPY rf.pkl /app
COPY templates /app/templates
COPY static/css2.css /app



# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
# Commande par défaut
CMD ["python", "predict.py"]
