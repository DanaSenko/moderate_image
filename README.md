# NSFW Image Moderation API

## Описание
Сервис на FastAPI для проверки изображений на нежелательный контент через https://rapidapi.com.

## Запуск
1. Клонируйте репозиторий
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Создайте файл `.env` и добавьте ваш ключ RAPIDAPI_KEY:
```
RAPIDAPI_KEY=ваш_ключ
```
4. Запустите сервер:
```
uvicorn main:app --reload
```

## Пример запроса
```
curl -X POST -F "file=@example.jpg" http://localhost:8000/moderate
```

## Ответы
- `{ "status": "OK" }` — если изображение безопасно
- `{ "status": "REJECTED", "reason": "NSFW content" }` — если найден неприемлемый контент

# Локальное тестирование - успешно


[![asciicast](https://asciinema.org/a/RsFRtC3B03O2VfVsnKlmpq0pb.svg)](https://asciinema.org/a/RsFRtC3B03O2VfVsnKlmpq0pb)
