# run elastic search and kibana on ports
sudo docker run -d --name es -p 2048:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.7.0
sudo docker run -d --name kibana --link es01-test:elasticsearch -p 4096:5601 docker.elastic.co/kibana/kibana:7.7.0