#! /bin/bash

echo "### configuring elasticsearch and kibana ###"
docker run -d --name es01-test -p 2048:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.7.0
docker run -d --name kib01-test --link es01-test:elasticsearch -p 4096:5601 docker.elastic.co/kibana/kibana:7.7.0
echo "Done"
