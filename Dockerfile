FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install -r requirement.txt
RUN pip install Flask-Bootstrap


CMD ["python", "app.py", "accueil.html", "base.html"]
