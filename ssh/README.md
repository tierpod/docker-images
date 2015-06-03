# ssh

Контейнер c supervisord+sshd внутри. Добавлено 2 пользователя:

* root, пароль root
* user, пароль user

SERVICE_NAME=ssh в docker-compose.yml указывает сервис, к которому
привяжется этот контейнер в consul.
