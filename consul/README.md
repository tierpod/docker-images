# consul with registrator

* [consul services](https://www.consul.io/intro/getting-started/services.html)
* [registrator](https://github.com/gliderlabs/registrator)
* [dnsmasq forward](http://pyther.net/2010/12/dns-conditional-forwarding-dnsmasq/)
* [всё вместе](https://www.airpair.com/scalable-architecture-with-docker-consul-and-nginx)

Содержит 2 image-а:

* consul:latest - для service discovery
* registrator:master - для автоматического добавления записей о запущенных
  контейнерах в consul. Нужен именно master из-за наличия в latest
  [бага](https://github.com/gliderlabs/registrator/issues/133)

Дополнительно, файл с конфигом для dnsmasq, чтобы все запросы на service.consul
перенаправлялись на consul dns: dnsmasq-consul. Для ubuntu 14.04 его достаточно
скопировать в /etc/NetworManager/ и перезапустить сервис:

```
service network-manager restart
```

Затем поднять эти 2 контейнера через docker-compose up и запустить, для примера,
соседний контейнер ssh - в логах регистратора увидим:

```
added: 43b44a63f93a 2b81bde81aee:ssh_ssh_1:22
```

Список сервисов можно посмотреть curl-ом (доступно [api](https://www.consul.io/docs/agent/http.html))

```
curl localhost:8500/v1/catalog/services
curl localhost:8500/v1/catalog/service/ssh
```

После этого можно обращаться к поднятым контейнерам по имени сервиса (см.
SERVICE_NAME в ssh/docker-compose.yml):

```
dig ssh.service.consul
...
;; ANSWER SECTION:
ssh.service.consul.	0	IN	A	172.17.0.51
```
