FROM python:3.10 
WORKDIR /code
COPY ./requirements.txt .
RUN pip install runpod
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./app/ .
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"] 
CMD ["python" , "/code/app/test_ping.py"]

# we have no module named app error for fastapi ??