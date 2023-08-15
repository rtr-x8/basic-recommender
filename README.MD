## install

```bash
cp .env.example .env
docker compose up -d --build
docker compose exec brs_python3 pip install -r requirements.txt
```

open localhost:8888

## add package

```bash
docker compose exec brs_python3 pip3 install xxx
docker compose exec brs_python3 python3 -m pip freeze > requirements.txt

```

## update package

```bash
docker compose exec brs_python3 pip install -r requirements.txt
```
