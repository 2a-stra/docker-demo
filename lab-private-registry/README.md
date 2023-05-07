# Docker private registry

<img src="private-registry.png" alt="private-registry" width="1024"/>

Контейнер с приложением на Docker Hub:

```
https://registry.hub.docker.com/_/registry
```

Запуск registry на локальном хосте на порту 5000:

``` bash
$ docker run -d -p 5000:5000 --restart always --name registry registry:2
```

Добавляем имя приватного репозитория `localhost` к нашему образу:

```bash 
$ docker tag portal-app:1.0 localhost:5000/portal-app:1.0
```

Загружаем образ в наш репозиторий:

```bash
$ docker push localhost:5000/portal-app:1.0
```

Запускаем контейнер используя образ из нашего приватного репозитория:

```bash
docker run \
-p 8001:8888 \
-e REDIS_HOST=redis-db \
-e REDIS_PORT=6379 \
-e APP_PORT=8888 \
--name portal-local \
localhost:5000/portal-app:1.0
```

Source: [portal-app:1.0](https://github.com/2a-stra/docker-demo/tree/main/lab2)