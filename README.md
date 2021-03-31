# video_content
[![video_content](https://github.com/AndIsaev/video_content/actions/workflows/main.yml/badge.svg)](https://github.com/AndIsaev/video_content/actions/workflows/main.yml)


<p><a href="https://www.python.org/" rel="nofollow"><img src="https://camo.githubusercontent.com/938bc97e6c0351babffcd724243f78c6654833e451efc6ce3f5d66a635727a9c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d507974686f6e2d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d507974686f6e" alt="Python" data-canonical-src="https://img.shields.io/badge/-Python-464646??style=flat-square&amp;logo=Python" style="max-width:100%;"></a>
<a href="https://www.djangoproject.com/" rel="nofollow"><img src="https://camo.githubusercontent.com/99e48bebd1b4c03828d16f8625f34439aa7d298ea573dd4e209ea593a769bd06/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d446a616e676f2d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d446a616e676f" alt="Django" data-canonical-src="https://img.shields.io/badge/-Django-464646??style=flat-square&amp;logo=Django" style="max-width:100%;"></a>
<a href="https://www.sqlite.org/index.html" rel="nofollow"><img src="https://camo.githubusercontent.com/2c46c2b57530e634094dcb5ca341adbd8cc101300fd0968991b2a2700f1ac318/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d53514c6974652d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d53514c697465" alt="SQLite" data-canonical-src="https://img.shields.io/badge/-SQLite-464646??style=flat-square&amp;logo=SQLite" style="max-width:100%;"></a>  
  

## Описание
Сайт, позволяющий загружать видео, смотреть его, получать их по api. Каждое видео выводится с watermarker.


## Задание:
- «+» развернуть Django
- «+» сделать возможность загрузки видео
- «+» вывести видеоплеер на странице
- «+» воспроизведение видеопотока (разделенного на части и с наложением Watermark)
- «+» настройка DRF API
- «+» настроить возможность получение видеопотока через API
- «+» разместить проект на GitHub

## Стек

```sh
- Python
- Django
- Django REST framework
- Bootstrap
- Sqlite
- Video.js
```

## Установка


Клонируем проект: 
```
git@github.com:AndIsaev/video_content.git
```

Создаем виртуальное окружение и активируем его:

```
python -m venv venv
source venv/Scripts/activate
```

Устанавливаем пакеты:

```
pip install -r requirements.txt
```

Делаем миграцию:

```
python manage.py migrate
```

## Использование

Запускаем приложение:

```
python manage.py runserver
```

Чтобы воспользоваться api-сервисом необходимо:

* Зарегестрироваться
* Сделать POST-запрос по ссылке http://127.0.0.1:8000/api/v1/token/
```
Вы получите примерно это:
    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4NzEyODUzNSwianRpIjoiNzRmMDhkOGEwODQ4NGEzYjgyZmM4MDRhMTQ3ZTEyZmIiLCJ1c2VyX2lkIjoxfQ.GW7Obcvy2TWgsEI5lqSx9BC1mxk0WnsywBHrXScs7bI",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg3MDQyNDM1LCJqdGkiOiI5ZmNjMWE5YTM5NDQ0Y2Q4OWJlOGFlOGRlYWQxNDE0ZSIsInVzZXJfaWQiOjF9.ZkEdzDN5pNgYToDRJq1CKHjIglK1ir1fhnfcXkmziuk"
    } 
```
* Наш токен "access". Теперь скопировав этот токен, вы мжете поолучить все посты с видео по ссылке:
http://127.0.0.1:8000/api/v1/content/


# Автор:
* [Андрей Исаев](https://github.com/AndIsaev)
