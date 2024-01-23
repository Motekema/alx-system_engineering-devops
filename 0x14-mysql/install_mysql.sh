#!/usr/bin/env bash
# Script to install MySQL on web-01 and web-02 servers

# Update package list and install MySQL server
sudo apt-get update
sudo apt-get install -y mysql-server-5.7

# Check MySQL version
mysql --version

# Ensure MySQL service is running
sudo service mysql status
