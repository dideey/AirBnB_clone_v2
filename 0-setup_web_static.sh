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
sudo echo "<html>
<head>
</head>
<body>
    Hoberton School
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
#Giving ownership of the '/data' folder to 'Ubuntu'(group and user)
sudo chown -R ubuntu:ubuntu /data/
#updating the Nginx configuration to serve the content of '/data/web_static/current/' to 'hbnb_static'
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service restart nginx
