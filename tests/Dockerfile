FROM python:3.9.16

# working directory
WORKDIR /usr/src/app

# copy requirement file to working directory
COPY tests/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY tests .

CMD [ "pytest", "."]