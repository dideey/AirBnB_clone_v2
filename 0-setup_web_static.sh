#!/usr/bin/env bash
#The script setsup my web servers for the deployment of web-static
#installs nginx if not already installed
if [ ! -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi
#creates the specified folders if they don't already exist
if [ ! -d "/data" ]; then
    sudo mkrdir "/data"
fi
if [ ! -d "/data/web_static/" ]; then
    sudo mkdir "/data/web_static/"
fi
if [ ! -d "/data/web_static/releases/" ]; then
    sudo mkdir "/data/web_static/releases/"
fi
if [ ! -d "/data/web_static/shared/" ]; then
    sudo mkdir "/data/web_static/shared/"
fi
if [ ! -d "/data/web_static/releases/test/" ]; then
    sudo mkdir "/data/web_static/releases/test/"
fi
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
</html>" > /data/web_static/releases/test/index.html
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
