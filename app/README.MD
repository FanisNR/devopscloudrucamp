для запуска в терминале:

0. (sudo)apt install make
1. sudo apt update
2. sudo apt install apt-transport-https ca-certificates curl software-properties-common
3. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
4. echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
5. sudo apt update
6. apt-cache policy docker-ce
7. sudo apt install docker-ce
8. sudo systemctl status docker



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

