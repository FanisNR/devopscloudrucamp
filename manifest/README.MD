1. sudo apt update
2. sudo apt upgrade
3. sudo apt install -y docker.io
4. sudo usermod -aG docker $USER
5. curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64
6. chmod +x ./kind
7. sudo mv ./kind /usr/local/bin/
8. kind --version
9. kind create cluster --name my-cluster
10. (sudo)kubectl apply -f cloud-manifest.yaml