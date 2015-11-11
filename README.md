# docker images

Несколько простых образов для docker-а. Чтобы запустить:

```
cd project
docker-compose up
```


## Зависимости

* docker
* docker-compose


## Настройка selinux (fedora 23)
Требуется для запуска xorg-приложений внутри docker-контейнера.

```
semodule -i docker-xorg-local.pp
```
