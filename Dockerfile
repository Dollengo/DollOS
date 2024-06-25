FROM python:3

WORKDIR /src/system/main/

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "DollOS.py" ]