# battery-demo

## tech stack

## installation

## testing

### setting up webserver watch

```
source .venv/bin/activate && uvicorn app.main:app --reload
```

### setting up tailwindcss watch (recompile css on change)

```
source .venv/bin/activate && tailwindcss -i ./app/static/src/tw.css -o ./app/static/css/main.css --watch

```
