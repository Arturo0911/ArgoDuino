FROM python:3.8.10
RUN pip install --upgrade pip
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "main.py"]