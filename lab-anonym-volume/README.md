# Anonymous volumes

## Просмотр смонтированного volume  в контейнере `redis-db`:

```bash
docker inspect redis-db

docker volume ls
docker volume inspect <volume_id>
```

## Подключение к volume из другого контейнера `alpine`:

```
docker run -it --rm \
-v <volume_id>:/data \
alpine sh

> ls /data
```