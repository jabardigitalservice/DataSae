FROM python:3.9.13-slim

EXPOSE 5025

COPY .requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./datasae/api /api

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "5025", "--workers", "4"]
