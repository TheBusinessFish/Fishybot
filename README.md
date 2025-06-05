# 🤖 FishyOcean Portfolio Bot

Профессиональный Telegram бот-портфолио разработчика. Демонстрирует услуги, принципы работы и примеры проектов.

## ✨ Особенности

- Информация удобно распределена по категориям

## ⚙️ Технологический стек

- Python 3.11
- Aiogram 3.0
- Asyncio
- Логгирование

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.11+
- Аккаунт в Telegram
- Токен бота от [@BotFather](https://t.me/BotFather)

### Установка

```bash
# Клонировать репозиторий
git clone https://github.com/FishyOcean/portfolio-bot.git
cd portfolio-bot

# Создать виртуальное окружение (рекомендуется)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows

# Установить зависимости
pip install -r requirements.txt
```

### Конфигурация

1. Создайте файл `.env` на основе примера:
   ```bash
   cp .env.example .env
   ```
2. Откройте `.env` в редакторе и добавьте токен бота:
   ```env
   TELEGRAM_TOKEN="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
   ```

### Запуск

```bash
python fishybot.py
```

## 🌐 Развертывание на сервере

### Вариант 1: Системный сервис (Linux)

```bash
# Создаем сервисный файл
sudo nano /etc/systemd/system/fishybot.service
```

```ini
[Unit]
Description=FishyOcean Portfolio Bot
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/path/to/bot
ExecStart=/path/to/venv/bin/python /path/to/bot/fishybot.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

```bash
# Запускаем сервис
sudo systemctl daemon-reload
sudo systemctl enable fishybot
sudo systemctl start fishybot

# Проверяем статус
sudo systemctl status fishybot
```

### Вариант 2: Docker

```Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "fishybot.py"]
```

```bash
docker build -t fishybot .
docker run -d --name fishy-bot --env-file .env fishybot
```

## 📝 Кастомизация

1. Отредактируйте текстовые переменные в `fishybot.py`
2. Обновите информацию о портфолио
3. Измените контакты в разделе `CONTACTS_TEXT`
4. Настройте модели ценообразования в `PRINCIPLES_TEXT`

## ⚠️ Важные замечания

- Никогда не храните токены в коде!
- Используйте файл `.env` и добавляйте его в `.gitignore`
- Для продакшн среды установите `LOG_LEVEL=WARNING`
- Регулярно обновляйте зависимости

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](LICENSE).
