FROM python:3.7-alpine
COPY . /app
WORKDIR /app

# Add files
ADD run.sh /run.sh
ADD entrypoint.sh /entrypoint.sh
ADD run.py /run.py
 
RUN chmod +x /run.sh /entrypoint.sh

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "/entrypoint.sh"]