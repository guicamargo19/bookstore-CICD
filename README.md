# Bookstore

Django project Bookstore App developed with Poetry.

Project developed in the Full Stack Python course at EBAC - Escola Britânica de Artes Criativas e Tecnologia - Brazil.

## ▶️ Prequisites

- Python 3.10
- Poetry
- Docker && Docker-Compose

## 🚀 Quickstart

1 - Clone this project:

  ```shell
  git clone https://github.com/guicamargo19/bookstore.git
  ```

2 - Install dependencies:

  ```shell
  cd bookstore
  poetry install
  ```

3 - Execute project:

  ```shell
  poetry run python manage.py migrate
  poetry run python manage.py runserver
  ```

Run docker dev server environment:

  ```shell
  docker-compose up -d --build 
  docker-compose run web python manage.py migrate
  ```

5. Run tests inside of docker:

  ```shell
  docker-compose run --rm web python manage.py test
  ```

## 🛠️ Tools used for the development of this project

* **Poetry** - Tool for managing packages and dependencies in Python.
* **Django** - Framework for fast web development, written in Python.
* **Docker** - Set of platform-as-a-service products that use operating system-level virtualization to deliver software in packages called containers.

## ✒️ Author

Guilherme Ferreira Camargo
