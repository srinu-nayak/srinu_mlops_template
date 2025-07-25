# srinu_mlops_template
creating a template for all kind of mlops projects

1. conda create -p venv/ python==3.10
2. conda activate venv/
3. template.py
4. requirements.txt
5. setup.py
Docker commands

docker build -t srinu0930/srinu_mlops_template .
docker images
docker push srinu0930/srinu_mlops_template:latest
docker image rm -f srinu0930/srinu_mlops_template:latest
docker pull srinu0930/srinu_mlops_template:latest
