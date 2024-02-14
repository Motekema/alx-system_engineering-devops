#!/usr/bin/env bash
# This script installs and configures the Datadog agent on the web-01 server

# Install the Datadog agent
DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=<DATADOG_API_KEY> DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"

# Configure the Datadog agent
sudo sed -i -e 's/# tags:/tags:\n  - environment:production/' /etc/datadog-agent/datadog.yaml
sudo sed -i -e "s/# hostname:/hostname: $(hostname)/" /etc/datadog-agent/datadog.yaml

# Restart the Datadog agent
sudo systemctl restart datadog-agent
