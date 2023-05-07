# Docker compose (lab3)

<img src="docker-compose.png" alt="docker-compose" width="1024"/>

Файл в формате YAML `portal.yaml` описывает запускаемые сервисы (контейнеры).

В файле yaml имеют значения одинаковые отступы для параметров одного уровня.

## Redis DB
```yaml
version: '3'
services:
  redis-db:        # container name
    image: redis:alpine
    volumes:
      - data-db:/data:rw

volumes:
  data-db:
    driver: local
```

## Web-app (backend) and web-server (proxy):
```
  portal-app:      # container name
    build: web     # build from Dockerfile in the "web" folder
    environment:
      - APP_PORT=8888
      - REDIS_HOST=redis-db
    volumes:
      - ./templates:/app/templates:ro
    depends_on:
      - redis-db

  nginx:           # container name
    image: nginx:alpine
    ports: 
      - 8000:8000
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - portal-app
```



### 1. Клонируйте проект:

```bash
git clone https://github.com/2a-stra/docker-demo.git
cd docker-demo
```

### 2. Измените имя папки `lab3` на папку с новым названием `docker-<name>`:

```bash
mv lab3 docker-<name>
cd docker-<name>
```

Это имя будет использоваться в именах сервисов.

### 3. Измените в файле `portal.yaml`:
- Nginx host port 8000


## Практическое задание 2

### 1. Запустите контейнеры с помощью `docker-compose`:

```bash
docker-compose -f portal.yaml up -d
```

### 2. Проверьте запущенные контейнеры:

```bash
docker ps
```

### 3. Проверьте список `volume` и `network`:

```bash
docker volume ls
docker network ls
```

### 4. Проверьте работу web-приложения через веб-интерфейс: http://localhost:8000

<img src="portal-app-list.png" alt="portal-app-list" width="320"/>

### 4.1 Проверка работы веб-приложения в терминале:

```bash
# Get users list
curl localhost:8000/list

# Create new user
curl -X POST -d 'user=Alice&password=123' http://localhost:8000/create

# Delete user
curl -X POST -d 'user=Alice' http://localhost:8000/delete
```

### 5. Остановите `docker-compose`:

```bash
docker-compose -f portal.yaml down
```

### 6. Проверьте список всех контейнеров:

```bash
docker ps -a
```
