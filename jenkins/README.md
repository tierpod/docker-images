# jenkins + jenkins-slave (dind)

## jenkins

Официальный image для jenkins. Домашняя директория указывает на ./jenkins_home/


## jenkins-slave (dind)

Docker-in-docker, позволяет запустить slave с docker-ом внутри. Его можно 
прописать сборщиком в jenkins с параметрами:

* hostname: jenkins_slave_1
* user: jenkins
* password: jenkins

Затем назначить какой-нибудь label этому слэйву, и в задаче поставить галку
"ограничить количество узлов, которые могут собирать этот проект". После чего
можно будет на этом slave-е, например, компилировать что-то внутри
докер-контейнеров.
