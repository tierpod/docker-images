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

```
semodule -i docker-xorg-local.te
```
