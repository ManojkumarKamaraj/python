FROM python

WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY app.py .

CMD ["python","app.py"]