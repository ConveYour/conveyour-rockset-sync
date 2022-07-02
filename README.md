### Getting Started

1. Add your Rockset API key and workspace to a .env file in root of project. 

```
cd ./conveyour-rockset-sync
code .env
```

```
ROCKSET_API_KEY=<Your KEY>
ROCKSET_WORKSPACE=acme_cy
```


2. Use docker compose to start the built in Python environment

```
# from ./
docker-compose up
```

3. bash into the docker container and try cy-rockset.py
```
docker exec -it cy_rockset_python bash
cd /code
python cy-rockset.py
```

The first query set to run is a summary of tables you have access to in your workspace. 

```
{'table': 'lessons', 'record_count': 1459}
{'table': 'campaigns', 'record_count': 108}
{'table': 'lesson_items', 'record_count': 7044}
{'table': 'lesson_progress', 'record_count': 2242370}
{'table': 'triggers', 'record_count': 1108}
{'table': 'contacts', 'record_count': 30025}
{'table': 'events', 'record_count': 10473873}
```