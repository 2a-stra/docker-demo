# Docker: named volume for Redis

<img src="named-volume.png" alt="named volume" width="1024"/>


## Практическое задание

### 1. Создайте новый volume с именем `redis-data`:

```bash
docker volume create redis-data

docker volume ls

docker volume inspect redis-data
```

### 2. Запустите контейнер `redis-db` с подключенным volume `redis-data`:

```bash
docker run -d --rm \
-v redis-data:/data:rw \
--name redis-db \
--net redis-network \
redis:alpine redis-server --save 60 1
```

### 3. Запустите контейнер с web-приложением и запишите новые данные в БД через веб-интерфейс порт `<8000>`:

[lab2 portal-app](https://github.com/2a-stra/docker-demo/tree/main/lab2)

```bash
docker build -t portal-app:1.0 .

docker run -d --rm \
-p 8000:8888 \
-e REDIS_HOST=redis-db \
-e REDIS_PORT=6379 \
-e APP_PORT=8888 \
--name portal-app \
--net redis-network \
portal-app:1.0
```

#### 3.1 Проверьте работу приложения с базой данных через web-интерфейс порт `<8000>`:

`http://localhost:8000`

Или в консоли:

```bash
# Get users list
curl localhost:8000/list

# Create new user
curl -X POST -d 'user=Alice&password=123' http://localhost:8000/create

# Delete user
curl -X POST -d 'user=Alice' http://localhost:8000/delete
```


### 4. Остановите контейнер `redis-db` и удалите его:

```
docker stop redis-db
(docker rm redis-db)
```

### 5. Создайте и запустите новый контейнер redis-db c тем же volume.

См. п. 2.

### 6. Проверьте, что данные в базе данных сохранились с прошлого запуска:

`http://localhost:8000`


## Общее файловое хранилище:

<img src="shared-file-storage.png" alt="shared-file-storage" width="480"/>

## Путь к файлам volume в Windows и MacOS 

<img src="linux-path.png" alt="linux-path" width="320"/>

```
# Windows WSL2:
\\wsl$\docker-desktop-data\data\docker\volumes

# MacOS:
screen ~/Library/Containers/com.docker.docker/Data/vms/0/tty
cd /var/lib/docker
```