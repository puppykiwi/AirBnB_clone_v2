#!/usr/bin/env bash
# this script will setup our webserver and deploy our code using fabric
sudo apt update
sudo apt install nginx -y

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu:ubuntu /data/

echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
	alias /data/web_static/current;
	index index.html index.htm;
    }

    location /redirect_me {
	return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    
}" | sudo tee /etc/nginx/sites-available/default

sudo service nginx restart
