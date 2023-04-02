[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# MarkingHack2023_Foxhound

## Описание

Решение команды Foxhound на хакатоне MarkingHack (https://hack.markirovka.ru/), 31 марта - 4 апреля 2023 г. Демонстрационное приложение доступно на http://foxhound-team.ru до конца хакатона. Веб-приложение обеспечивает демонстрацию возможностей алгоритмов, реализованных командой, по анализу открытых данных системы "Честный знак", предоставленных организаторами.

## Развёртывание

1. Установить [docker  и docker compose](https://docs.docker.com/engine/install/ubuntu/).
2. В папке compose создать файл .env и [заполнить](#описание-переменных-окружения) его в соответствии с примерами.
3. Запустить команду docker compose up -d с правами суперпользователя:
```bash
sudo docker compose -f docker-compose.prod.yml up -d
```

## Структура каталогов

* `backend` - файлы бекенда
* `frontend` - файлы фронтенда на Vuejs + Vuetify
* `compose` - файлы Docker и файлы конфигурации http-прокси автоматизации развёртывания
* `research` - файлы jupyter и python для анализа данных, отладки и демонстрации алгоритмов обработки
* `docker-compose.yml` - файл docker compose для автоматизации развёртывания веб-приложения с помощью docker compose

## Команда

* Антон Недогарок - анализ данных (Python, Pandas, SciPy, Jupyter), фронтенд (VueJS, Vuetify)
* Зеленовский Сергей - анализ данных (Python, Pandas, SciPy, Jupyter)
* Петров Антон - бэкенд, Python
* Файзуллин Фарис - анализ данных (Python, Pandas, SciPy, Jupyter)
