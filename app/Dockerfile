FROM python:3.11-slim
WORKDIR /code
RUN mkdir -p app
COPY . /code/app
RUN pip install --no-cache-dir -r app/requirements.txt 
EXPOSE 8000 
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]


