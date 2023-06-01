# Docker JS web application

<img src="js-web-app.png" alt="js-web-app" width="1024"/>

## Сеть Docker network

<img src="docker-network.png" alt="docker-network" width="480"/>

## Практическое задание

### 1. Создайте отдельную сеть для контейнеров

```bash
docker network ls
docker network create network-<nickname>
```

### 2. Отредактируйте имя `host` в файле `server.js`

```javascript
  host: 'redis-<nickname>',
```

### 3. Создайте новый образ с веб-приложением:

```bash
docker build -t js-app-<nickname>:1.0 .
```

Последний параметр в команде - точка ".", означает что `Dockerfile` находится в текущей директории.

После создания новый образ должен появится в списке `docker images`.


### 4. Запустите контейнер `redis-<>`:

```bash
docker run -d --rm \
--name redis-<> \
--net network-<> \
redis:alpine redis-server --save 60 1
```

Используйте имя сети `network-<>` созданное на шаге 1.

### 5. Запустите контейнер c именем `js-<nickname>` из созданного образа `js-app-<>` на порту `<8000>`:

```bash
docker run -d --rm \
-p 8000:5000 \
--name js-<nickname> \
--net network-<> \
js-app-<nickname>:1.0
```

Имя сети должно быть такое же как в предыдущем шаге.

### 6. Сделайте запрос к БД через веб-интерфейс:

`http://localhost:8000/`

Или через консоль:

```bash
curl localhost:8000
```

### 7. Подключитесь через интерактивный терминал к запущенному контейнеру:

```bash
docker exec -it js-<> sh
```

Проверьте содержимое рабочего каталога:
```bash
ls -l
```

### 8. Проверьте лог сообщений и список запущенных процессов:

```bash
docker logs js-<>
docker top js-<>
```

[Source](https://github.com/docker/awesome-compose/tree/master/nginx-nodejs-redis)