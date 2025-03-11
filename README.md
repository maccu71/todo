From Simple Python App to Full Kubernetes Microservice Journey 🦊🚀

Welcome to the Sly as a Fox App, where Maciej crushes one comfort zone after another, aiming to become the Grandmaster - Prophet of Microservices. Watch as he crafts microservices like a famous cook prepares gourmet meals in a microwave — fast, efficient, and surprisingly powerful!

This project starts as a simple Python TODO app, and the goal is to transform it into a fully-fledged microservice architecture using:

    Flask for the web application
    Databases (SQL/NoSQL) for data storage
    Python for the core application logic
    Docker containers for packaging
    Kubernetes for orchestration and scaling

This journey takes you from zero to hero, expanding knowledge in modern software development, continuous integration, and deployment pipelines.
🚀 Features

    Simple Python App: We begin with a small, functional Python TODO app.
    Flask Microservice: As we grow, we break out the app into a Flask-based microservice for handling API requests.
    Databases: Add databases — either SQL or NoSQL — for data persistence and manage user data efficiently.
    Dockerize: Learn how to containerize the app with Docker, ensuring scalability and easy deployment.
    Kubernetes Deployment: Finally, we take it to the cloud with Kubernetes, deploying and scaling our app across multiple pods, ensuring reliability and performance.

🛠️ Setup

To run this project on your local machine:
1. Clone the repository

git clone https://github.com/maccu71/todo.git
cd todo

2. Set up your environment

Install the required dependencies (e.g., Python, Flask, Docker) using pip:

pip install -r requirements.txt

3. Dockerize the app

Build the Docker image for the app:

docker build -t todo-app .

Run the container:

docker run -p 5000:5000 todo-app

4. Deploy to Kubernetes (WIP)

In the future, we’ll deploy this app to a Kubernetes cluster for better scalability and management.

kubectl apply -f k8s/deployment.yaml

🧑‍💻 Workflow

This project is built with continuous integration in mind. We'll be using GitHub Actions to automate the build, test, and deploy processes as we evolve the app.
GitHub Actions (CI/CD)

    Build: The app will be built inside a Docker container whenever new changes are pushed.
    Test: We’ll automate testing to make sure each microservice is performing as expected.
    Deploy: Every successful build will automatically deploy to our Kubernetes cluster.

Future Development

    Integration of more advanced microservices.
    Adding more complex database architectures.
    Automating deployments to multiple environments (Dev, Prod, Staging).
    Monitoring and logging services (e.g., Prometheus, Grafana).
    Scaling the app to handle more traffic.

🌱 Contributing

Feel free to contribute by forking this repository, opening pull requests, or submitting issues! All contributions are welcome, and we encourage you to get involved as we journey through the world of microservices.
👨‍🏫 Inspiration

    Maciej: Who else but Maciej to lead this journey and turn a simple app into a scalable, robust, microservice-based system!
    The journey: Watch the evolution of this app as we explore Kubernetes, Docker, and Flask in real-time.

😎 Final Thoughts

The journey from a Simple Python App to a Full Kubernetes Microservice might be long, but it’s incredibly rewarding! It’s a journey where you’ll learn how to manage microservices like a master chef, creating complex systems with the efficiency of a microwave.

Welcome to the Sly as a Fox App. Let’s turn those comfort zones into history! 🦊💥
