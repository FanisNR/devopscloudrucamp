#!/bin/bash

# Команда для установки Ansible 
sudo apt update 
sudo apt install ansible -y

playbook="cloudru-setup.yml"

# Проверка наличия playbook
if [ ! -f "$playbook" ]; then
    echo "Playbook не найден по пути: $playbook"
    exit 1
fi

# Запуск playbook
ansible-playbook -i inventory.ini "$playbook"
