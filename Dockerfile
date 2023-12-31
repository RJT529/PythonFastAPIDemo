FROM python:3.9
WORKDIR /code
COPY . .
RUN pip3 install -r requirements.txt
CMD ["/bin/bash", "-c", "cd app; uvicorn controller:app --host 0.0.0.0 --port 80"]