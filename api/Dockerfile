FROM python:3.8-slim

ENV DATABASE_URL ${DATABASE_URL}

RUN mkdir -p /usr/src/app/api
WORKDIR /usr/src/app/api

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/entrypoint.sh"]