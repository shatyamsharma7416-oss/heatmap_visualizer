FROM python:3

WORKDIR /user/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ..

EXPOSE 10000

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=10000"]

