FROM python:3
RUN mkdir ~/.cache
RUN chmod -R 777 ~/.cache
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
CMD [ "python", "app.py"]
EXPOSE 5000