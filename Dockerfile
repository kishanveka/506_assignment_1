FROM python:3.9-slim-buster
RUN pip3 install Flask
WORKDIR /app
CMD ["python3", "/app/app.py"]
