#

## Контейнер для изоляции приложений

<img src="images/docker_logo.png" alt="docker-logo" width="320"/>

- Изолированное окружение (файловая система, процессы, сеть)
- Конфигурационные файлы
- Зависимости
- Стартовый скрипт

<img src="images/containers_1.jpg" alt="containers" width="600"/>


## Docker Inc.

2013 — Опубликован код Docker под открытой лицензией Apache 2.0

(Community Edition)

Enterprise Edition — Проприетарная лицензия Docker Inc.

## Виртуализация

<img src="images/virtualization.png" alt="virtualization" width="1024"/>

- VMware ESXi
- Microsoft Hyper-V
- Linux KVM
- XEN

## Контейнерная изоляция

<img src="images/vm_docker.png" alt="vm_docker" width="720"/>

1. Контейнер меньше «весит»
2. Контейнер быстрее запускается
3. Контейнер требует меньше ресурсов

## Облачные провайдеры

<img src="images/cloud.jpg" alt="cloud.jpg" width="1024"/>

## Архитектура Docker

<img src="images/architecture.png" alt="architecture.png" width="720"/>

## Различие между образом (Image) и контейнером

<img src="images/docker_build.png" alt="docker_build.png" width="720"/>

## Слои образа

<img src="images/image_layers.png" alt="image_layers.png" width="600"/>

## Docker Hub

[hub.docker.com](https://hub.docker.com/search?q=)

- Official images
- Versions
- Tags

## Жизненный цикл контейнера

<img src="images/lifecycle.png" alt="lifecycle.png" width="720"/>

## Workflow

<img src="images/workflow.png" alt="workflow.png" width="720"/>

## Подключение в серверу по SSH

```
$ ssh -i .ssh/<mykey> <user>@<server.domain>
```

<img src="images/ssh.png" alt="ssh.png" width="600"/>


Создание пары ключей (Git-bash for Windows):

```bash
$ mkdir ~/.ssh

$ ssh-keygen.exe
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/Andrey/.ssh/id_rsa): .ssh/mykey
Enter passphrase (empty for no passphrase):
Enter same passphrase again:

# private and public keys
$ ls -a .ssh/
mykey  mykey.pub

# add public key to the server
(server)$ cat >> ~/.ssh/authorized_keys
```

## Установка Docker Desktop

Скачать приложение Docker Desktop для Windows 10/11 или MacOS:

[https://docs.docker.com/desktop/](https://docs.docker.com/desktop/)

### Для WINDOWS:

Установка и обновление WSL2:

[https://learn.microsoft.com/en-us/windows/wsl/install-manual](https://learn.microsoft.com/en-us/windows/wsl/install-manual)

Включение функций виртуализации:

[https://docs.docker.com/desktop/troubleshoot/topics/#virtualization](https://docs.docker.com/desktop/troubleshoot/topics/#virtualization)

Включение виртуализации в BIOS:

[https://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html](https://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html)

<img src="images/desktop.png" alt="desktop.png" width="320"/>

```bash
$ docker -v
```

## Запуск первого контейнера

```bash
$ docker run hello-world
```

## VSCode - Docker extension

<img src="images/vscode.png" alt="vscode.png" width="720"/>
