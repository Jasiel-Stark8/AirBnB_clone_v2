#!/usr/bin/env bash
# This script sets up 251279-web-01	ubuntu@18.204.5.218 & 251279-web-02	ubuntu@100.26.218.215 to deploy web_static

# Install Nginx if not installed
sudo apt-get update
sudo apt-get -y install nginx

# Create required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link. If it exists, remove and recreate
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content
sudo sed -i "38i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
