FROM python:3.6-buster
WORKDIR /newsapp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "start.sh"]