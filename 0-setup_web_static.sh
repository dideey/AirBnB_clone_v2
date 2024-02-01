#!/usr/bin/env bash
#The script setsup my web servers for the deployment of web-static
#installs nginx if not already installed
    sudo apt-get update
    sudo apt-get install -y nginx
    sudo ufw allow 'Nginx HTTP'
#creates the specified folders if they don't already exist

    sudo mkdir -p "/data"

    sudo mkdir -p "/data/web_static/"

    sudo mkdir -p "/data/web_static/releases/"

    sudo mkdir -p "/data/web_static/shared/"

    sudo mkdir -p "/data/web_static/releases/test/"

    sudo touch /data/web_static/releases/test/index.html
#creates a simple html file for testing purposes
echo "<!DOCTYPE html>
<html>
<head>
    <title>Simple file</title>
</head>
<body>
    <h1>Hello i'm Diddy</h1>
    <p1>Testing</p1>
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html
#removes symbolic link if any
rm -f /data/web_static/releases/test
#creates a new link
ln -s /data/web_static/current /data/web_static/releases/test/
#Giving ownership of the '/data' folder to 'Ubuntu'(group and user)
sudo chown -R ubuntu:ubuntu /data/
#updating the Nginx configuration to serve the content of '/data/web_static/current/' to 'hbnb_static'
# Nginx configuration file path
nginx_config="/etc/nginx/sites-available/default"
# Alias configuration
alias_config="location /hbnb_static/ {
    alias /data/web_static/current/;
    index index.html;
}"
#updating the aliasconfig to nginxconfig
sudo sed -i "/server {/a $alias_config" "$nginx_config"
#restarting nginx
sudo systemctl restart nginx
