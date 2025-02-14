<!-- PROJECT LOGO -->
<div align="center">
  <h2>mailganer-test</h2>

  <h3 align="center">README тестового задания</h3>

  <p align="center">
    Веб-приложение на Django (Python 2.7 / Django 1.9.9), небольшой сервис отправки имейл рассылок
  </p>
</div>

<a name="readme-top"></a>

<hr>

<!-- ABOUT THE PROJECT -->
## About The Project

Требования:
* Отправка рассылок с использованием html макета и списка подписчиков.
* Для создания рассылки использовать ajax запрос. Форма для создания рассылки заполняется в модальном окне. Использовать библиотеки: jquery, bootstrap.
* Отправка отложенных рассылок. (Отложенные отправки реализовать при помощи Celery)
* Использование переменных в макете рассылки. (Пример: имя, фамилия, день рождения из списка подписчиков).
* Отслеживание открытий писем.


### Built With

* [![Django][Django-badge]][Django-url]
* [![Postgres][Postgres-badge]][Postgres-url]
* [![Celery][Celery-badge]][Celery-url]
* [![Docker][Docker-badge]][Docker-url]
* [![Bootstrap][Bootstrap-badge]][Bootstrap-url]
* [![JQuery][JQuery-badge]][JQuery-url]


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Copy project to repository on local machine (HTTPS or SSH)
  ```sh
  git clone https://github.com/SuperLalka/mailganer-test.git
  ```
  ```sh
  git clone git@github.com:SuperLalka/mailganer-test.git
  ```

### Installation

To start the project, it is enough to build and run docker containers.
Database migration and fixture loading will be applied automatically.

1. Build docker containers
   ```sh
   docker-compose -f docker-compose.yml build
   ```
2. Run docker containers
   ```sh
   docker-compose -f docker-compose.yml up -d
   ```

### Documentation

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Django-badge]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://docs.djangoproject.com/
[Postgres-badge]: https://img.shields.io/badge/postgresql-%234169E1.svg?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
[Celery-badge]: https://img.shields.io/badge/celery-%2337814A.svg?style=for-the-badge&logo=celery&logoColor=white
[Celery-url]: https://docs.celeryq.dev/
[Docker-badge]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[Bootstrap-badge]: https://img.shields.io/badge/bootstrap-%237952B3.svg?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com/
[JQuery-badge]: https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com/
