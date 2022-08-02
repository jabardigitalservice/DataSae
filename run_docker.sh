#!/bin/bash
imageName=api_dqf:latest
containerName=api_dqf_container

docker build -t $imageName -f Dockerfile  .

echo stop and clear container...
docker stop $containerName
docker rm -f $containerName

echo docker-compose...
#docker-compose -f docker-compose.yml up -d
docker run --name $containerName -p 5025:5025 $imageName