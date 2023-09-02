0. sudo snap install helm --classic

1. helm install app-name helm/ 
# по умолчанию

2. helm install app-name2 helm/ -f prod_values.yaml
# при необходимости изменения  данных

3. helm install app-name2 helm/ --set containers.image=webimage2:version2
# при необходимости изменения  данных без создания нового 
# 2 и 3 команды можно комбинировать