sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
exit
gcloud compute scp D:\Flask-gke-app\app.py D:\Flask-gke-app\requirements.txt D:\Flask-gke-app\Dockerfile docker-vm-app:/home/sai_masetti_42gears_com/
exit
docker build -t flask-gke-app .
docker run -d -e BUCKET_NAME=sai-vinay-flask -p 80:80 flask-gke-app
