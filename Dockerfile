FROM python:3.10 
WORKDIR /code
COPY ./requirements.txt /code/
RUN pip install runpod
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
