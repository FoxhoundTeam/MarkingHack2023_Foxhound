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

