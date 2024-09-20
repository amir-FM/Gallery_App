FROM alpine:edge

RUN apk add --update py3-pip
RUN python3 -m venv /venv

ENV PATH="/venv/bin:$PATH"

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

COPY app.py .
COPY templates/ ./templates/
COPY public/ ./public

EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]
