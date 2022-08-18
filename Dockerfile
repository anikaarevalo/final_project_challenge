FROM python:3
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . . 
ENTRYPOINT ["python3"]
CMD ["app.py"]