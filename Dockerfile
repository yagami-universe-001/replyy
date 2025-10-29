FROM python:3.12-slim

# set workdir
WORKDIR /app

# copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY autoleech.py .

# run the bot
CMD ["python3", "autoleech.py"]
