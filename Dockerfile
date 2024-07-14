FROM python
WORKDIR /app
COPY . /app
RUN pip install -r requirement.txt
CMD ["python","app.py"]