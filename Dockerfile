# Kasutame ametlikku Python 3.9-põhist pilti
FROM python:3.9-slim

# Seame töökaustaks /app
WORKDIR /app

# Kopeerime requirements.txt faili konteinerisse
COPY requirements.txt /app/

# Paigaldame vajalikud Python sõltuvused
RUN pip install --no-cache-dir -r requirements.txt

# Kopeerime kogu projekti failide sisu konteinerisse
COPY . /app/

# Seame keskkonnamuutujad, et Django ei üritaks serverit otse käivitada
ENV PYTHONUNBUFFERED 1

# Seame käivituskomandi, et käivitada Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
