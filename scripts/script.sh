
#!/bin/bash
set -e

echo "=== Updating package lists ==="
sudo apt-get update -y

echo "=== Installing SSM Agent if missing ==="
if ! snap list amazon-ssm-agent >/dev/null 2>&1; then
    sudo snap install amazon-ssm-agent --classic
fi

echo "=== Enabling SSM Agent ==="
sudo systemctl enable snap.amazon-ssm-agent.amazon-ssm-agent.service

echo "=== Restarting SSM Agent ==="
sudo systemctl restart snap.amazon-ssm-agent.amazon-ssm-agent.service

echo "=== Checking SSM Agent status ==="
sudo systemctl --no-pager --full status snap.amazon-ssm-agent.amazon-ssm-agent.service

echo "=== Recent SSM Agent logs ==="
sudo journalctl -u snap.amazon-ssm-agent.amazon-ssm-agent.service -n 20 --no-pager

echo "=== SSM Agent setup completed ==="
echo "Check AWS Systems Manager > Fleet Manager > Managed nodes."
