# user python 3.10.11 as base image
FROM python:3.10.11-slim-buster
WORKDIR /usr/src/app

# install dependencies  (requirements.txt)
COPY requirements.txt ./    
RUN pip install --no-cache-dir -r requirements.txt

# copy the app  
COPY . .

#开放端口
EXPOSE 2333

# run the app use flask
CMD ["python","gui.py"]

# docker build -t lilei123/gpt-service:v2 .
# docker run -it -p 5000:5000 lilei123/gpt_service:v2
# docker push lilei123/gpt-service:v2
