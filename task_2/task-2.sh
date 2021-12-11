# sudo docker network create elastic

# # Starting Elasticsearch container for development or testing, run:
# sudo docker run --name es01-test --net elastic -p 127.0.0.1:2048:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.10.0 &

# #  start Kibana and connect it to your Elasticsearch container, run the following commands in a new terminal session
# sudo docker run --name kib01-test --net elastic -p 127.0.0.1:4096:5601 -e "ELASTICSEARCH_HOSTS=http://es01-test:9200" docker.elastic.co/kibana/kibana:7.10.0 &

sudo docker stop es01-test
sudo docker stop kib01-test
sudo docker network rm elastic
sudo docker rm es01-test
sudo docker rm kib01-test