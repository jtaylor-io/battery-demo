# battery-demo

## tech stack

- [FastAPI](https://fastapi.tiangolo.com/): Modern Fast Web Framework (Python)
- [TinyDB](https://tinydb.readthedocs.io/en/latest/index.html): Tiny, document oriented database (Python)(NOT FOR PRODUCTION!)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/): Jinja is a fast, expressive, extensible templating engine.
- [Tailwind CSS](https://tailwindcss.com/): A utility-first CSS framework (installed via [pytailwindcss](https://pypi.org/project/pytailwindcss/))
- [htmx](https://htmx.org/): Build modern UIs with power of hypertext.

## installation

### setting up virtual env

```
python -m venv .venv && source .venv/bin/activate
```

### load deps

```
python -m pip install -r requirements.txt
```

### setting up webserver watch

```
source .venv/bin/activate && uvicorn app.main:app --reload
```

### setting up tailwindcss watch (recompile css on change)

```
source .venv/bin/activate && tailwindcss -i ./app/static/src/tw.css -o ./app/static/css/main.css --watch

```

## deployment

### docker

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
  - Note: launching Docker Desktop starts the Docker daemon (Green whale in bottom left = running)

#### build

```
docker build -t battery-demo .
```

#### run locally

```
docker run -d -p 8000:80 battery-demo # adjust the port-mapping if you something else is running on port 8000
```

#### open browser and navigate to `localhost:8000`
