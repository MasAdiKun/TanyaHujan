#DOCKER FILE
FROM python:3.10
# Allow statements and log messoges to inmediat
ENV PYTHONUNBUFFERED True

ENV PORT=8080
# Copy local code to the container image.
ENV APP_HOME /back-end
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 rainpred:app