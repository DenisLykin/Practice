# Автор: 
Лыкин Денис
# Тестовое задание Python: 
Реализовать сервис, который принимает и отвечает на HTTP запросы
# Подготовительные действия
1. Установить Python 3.12.4

2. Клонировать проект и перейти в папку с проектом, для это нужно ввести команды в командной строке Windows:
```
git clone https://github.com/DenisLykin/Practice.git
cd Practice
```
3. Создать и активировать виртуальную среду:
```
python -m venv venv
venv\Scripts\activate.bat
```
4. Установить модули из файла requirements.txt:
```
pip install -r requirements.txt
```
5. Создать пустую БД в Postgresql
6. Зайти в файл myproject/setting.py и изменить в DATABASES параметры: 'NAME', 'USER', 'PASSWORD', на те, которые вы задали при создании пустой БД (либо же создать пустую с БД с аналогичными параметрами)
7. Сделать миграции БД:
```
python manage.py makemigrations
python manage.py migrate
```
8. Загрузить имеющиеся объекты БД или создать в /admin/
```
python manage.py loaddata fixtures/data.json
```
Для использования admin, нужно создать суперпользователя:
```
python manage.py createsuperuser 
```
9. Запустить сервер
```
python manage.py runserver
```
10. Перейти по http ссылке и добавить к ней, для проверки задания:
```
/city/
/city/<int:city_id>/street/
/shop/
/shop/?street=&city=&open=0/1
```
