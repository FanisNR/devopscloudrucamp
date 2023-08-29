для запуска в терминале:

1. (sudo)make build
# докер подтянет image c python, соберет новую image (webimage) и соберет контейнер (web)

2. (sudo)make run ИЛИ make debug
# запустит контейнер. для run - как бекграунд процесс. для debug - привязка процесса к терминалу, а также есть перехват stderr.

3. проверка:

* curl http://localhost:8000/hostname
* curl http://localhost:8000/author
* curl http://localhost:8000/id

<!-- curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:8000/hostname

curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:8000/author

curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:8000/id -->

