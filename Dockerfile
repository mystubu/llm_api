FROM python:3.10 
WORKDIR /
ADD ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
ADD ./app ./app
CMD ["python" , "-u",  "app/main.py"]

