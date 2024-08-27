apt get update -y
apt get upgrade -y
apt -y install docker.io
apt -y install docker-compose
docker-compose up -d
open "http://localhost:8000/docs"
