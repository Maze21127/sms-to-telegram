# Installation
1. Установить Python
2. Создать файл .env
```
API_ID=
API_HASH=
BOT_TOKEN=
CHANNEL_ID=
```
3. Создать приложение на сайте https://my.telegram.org/
4. Вставить API_ID и APi_HASH в .env
5. Установить необходимые библиотеки  
```pip install -r requirements.txt```


# First Start
1. Создать канал и написать в него любое сообщение
2. Переслать этому боту сообщение из канала https://t.me/getmyid_bot
3. Добавить ID канала в .env
4. Создать бота по этой ссылке https://t.me/BotFather
5. Добавить токен в .env

# Run Script
```python main.py message```

# Create Executable
```python setup.py build```