# Backup and Restore images

## Cохранить образ в файл tar:

```bash
docker save -o portal-app.tar portal-app:1.0

ls -l
tar tf portal-app.tar
```

## Удалить образ:

```bash
docker rmi portal-app:1.0
docker images
```

## Восстановить образ из tar-файла:

```bash
docker load -i portal-app.tar
docker images
docker history portal-app:1.0
```


# Export / Import containers

## Экспортировать контейнер в архив и скопировать на удаленный сервер:

```bash
$ docker export web2 | gzip > web2.gz

$ scp web2.gz <server>:~/.data
```

## Восстановить образ и запустить контейнер:

```bash
$ zcat web2.gz | docker import - nginx-index:v1

$ docker history nginx-index:v1   		# no layers history

$ docker run -d --rm -p 8000:80 --name web2 \
nginx-index:v1 /usr/sbin/nginx -g 'daemon off;'

$ curl http://localhost:8000
```

## Добавить команду CMD:

```bash
$ docker commit --change='CMD ["/usr/sbin/nginx", "-g", "daemon off;"]' \
web2 nginx-index:v2

$ docker history nginx-index:v2

$ docker stop web2

$ docker run -d --rm -p 8000:80 --name web2 nginx-index:v2
```