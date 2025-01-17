FROM python:3.7-alpine
WORKDIR /opt/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD python3 -m flask run --host=0.0.0.0 --port=80
EXPOSE 80
