
**Flask + MongoDB Learning Project — Work in Progress!**

Welcome to our humble playground for learning Flask 🐍, MongoDB 🍃, and refreshing how to dockerize apps like pros!

⚠️ Note: This project is in its initial phase, under active development, and evolving as we explore, break, and fix things to understand how everything works together.

**Project Goals:**

    Learn Flask basics — routes, templates, and forms.
    Connect Flask with MongoDB (via PyMongo) to store and retrieve data.
    Dockerize the app using Docker and Docker Compose.
    Practice building Docker images and running multi-container apps.
    Refresh docker-compose.yml and understand how to link services.
    Get comfortable with debugging running containers.

**Project Structure:**

```
.
├── app.py                 # Main Flask application
├── docker-compose.yml     # Docker Compose file to run Flask & MongoDB together
├── Dockerfile             # Docker image definition for Flask app
├── README.md              # You're here!
└── templates/             # Jinja2 templates for Flask frontend
    ├── about.html
    ├── home.html
    ├── items.html
    ├── layout.html
```

**Tech Stack:**

    Python 3.11-slim (Flask backend)
    MongoDB (NoSQL database)
    Docker & Docker Compose (Containerization)

**How to Run (Step by Step)**

1) Clone this repo (assuming you want to contribute or test):
```
git clone https://github.com/maccu71/todo.git
cd todo/
```
2) Build and start the containers:
`docker compose up --build`

This command will:

- Build the Flask app image.
- Start MongoDB and Flask containers.
- Connect them inside a Docker network.

You will see something like that:
```
todo$ docker compose up --build
Compose now can delegate build to bake for better performances
Just set COMPOSE_BAKE=true
[+] Building 18.1s (12/12) FINISHED                                                                             docker:default
 => [web internal] load build definition from Dockerfile                                                                  0.0s
 => => transferring dockerfile: 310B                                                                                      0.0s
 => [web internal] load metadata for docker.io/library/python:3.11-slim                                                   2.8s
 => [web auth] library/python:pull token for registry-1.docker.io                                                         0.0s
 => [web internal] load .dockerignore                                                                                     0.0s
 => => transferring context: 2B                                                                                           0.0s
 => [web 1/5] FROM docker.io/library/python:3.11-slim@sha256:[...]]                                                       0.0s
 => [web internal] load build context                                                                                     0.0s
 => => transferring context: 2.82kB                                                                                       0.0s
 => CACHED [web 2/5] WORKDIR /app                                                                                         0.0s
 => [web 3/5] COPY app.py .                                                                                               0.0s
 => [web 4/5] COPY templates/ .                                                                                           0.0s
 => [web 5/5] RUN pip install Flask pymongo                                                                              15.0s
 => [web] exporting to image                                                                                              0.2s
 => => exporting layers                                                                                                   0.2s
 => => writing image sha256:51[...]]                                                                                      0.0s
 => => naming to docker.io/library/todo-web                                                                               0.0s
 => [web] resolving provenance for metadata file                                                                          0.0s
[+] Running 5/5
 ✔ web                       Built                                                                                        0.0s
 ✔ Network todo_default      Created                                                                                      0.0s
 ✔ Volume "todo_mongo-data"  Created                                                                                      0.0s
 ✔ Container todo-mongo-1    Created                                                                                      0.0s
 ✔ Container todo-web-1      Created                                                                                      0.0s
Attaching to mongo-1, web-1
```

3) Access the app:

- Open a browser and go to: `http://localhost:5000`
- Navigate to /items to see stored items from MongoDB.
- Use `/update` to add a new item via form.

MongoDB Access (Optional) — if you wanna peek inside DB:

`docker exec -it docker-mongo-1 mongosh`

Then:
```
use my_database
show collections
db.my_collection.find().pretty()
```
**Flask App Routes Overview:**

| Route        | Methods            | Description                                   |
|--------------|--------------------|-----------------------------------------------|
| `/`          | GET                | Homepage displaying a welcome message.        |
| `/about`     | GET                | About page with general information.          |
| `/items`     | GET                | Displays all items stored in MongoDB.         |
| `/update`    | GET, POST          | Form to add a new item to MongoDB.            |


**Features (Current & Planned):**

- Display items from MongoDB
- Add new items via web form
- Delete & update items (Coming soon!)
- Authentication/Authorization (Maybe later?)
- Tests and CI pipeline (Future goal)
- Add authentication?

**Important Notes:**

This project is for learning purposes only — expect bugs, broken things, and a lot of fun fixing them!
MongoDB runs without authentication — DO NOT use this in production.
Contributions, suggestions, and ideas are welcome — just open an issue or PR!

**Example Database Content (Manual Access):**

```
[
  {
    "_id": ObjectId('67d45c992df47a7f8351e944'),
    "name": "Maciek",
    "description": "Learning Flask and MongoDB like a boss"
  },
  {
    "_id": ObjectId('67d45dc82df47a7f8351e945'),
    "name": "Maciek",
    "description": "Interesting stuff!"
  }
]
```
**Next Steps for Us:**

Add ability to delete/update items.
Add MongoDB initialization with seed data.
Docker health checks & production-ready tweaks.
Deploy example on AWS or Kubernetes cluster.
Add authentication.

**Contact & Ideas:**

If you have ideas or wanna laugh at our mistakes — ping us!