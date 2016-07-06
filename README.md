# docker images

Несколько простых образов для docker-а. Чтобы запустить:

```
cd project
docker-compose up
```


## Зависимости

* docker
* docker-compose


## x11apps containers

Требуется настройка xhost:

```
SI:localuser:root
```


## Настройка selinux

Требуется для запуска xorg-приложений внутри docker-контейнера:
```
semodule -i docker-xorg-local.pp
```
