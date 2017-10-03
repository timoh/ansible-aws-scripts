# Ansible scripts for AWS

## Example usage:

* ansible-playbook -i ./aws/ec2.py ./aws/start_scheduler.yml
* ansible-playbook -i ./aws/ec2.py ./aws/stop_scheduler.yml

## Add the EC2 instances to your inventory

The inventory file (e.g. aws_inventory in the root folder) should contain the public IP's of your EC2 instances. Otherwise Ansible doesn't know where to connect to. 
