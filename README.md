####################
What you need to do at the moment is:
- have installed Docker `https://docs.docker.com/engine/install/`
- clone this repository `git clone https://github.com/maccu71/todo` and `cd` into this `todo/`
- start building the image: `docker build -t todo-app .` <== the image will be created
- run the container from the image: `docker run -it todo-app:latest` <== this way you'll interact with the todo app

```
You'll see something like this:

docker run -it todo-app:latest

Co chcesz zrobić?
1. Utwórz nowe zadanie
2. Zobacz wszystkie zadania
3. Usuń zadanie
4. Wyjdź z programu
```
####################