# ansible-aws-scripts

> Ansible scripts related to setting up AWS EC2 instances for Apache Airflow etc.

## Prerequisites

1. Ensure you have the basic CLI tooling such as Python 2 / 3 installed, and for AWS you need an AWS account and access tokens etc.
2. Install ansible at http://docs.ansible.com/ansible/latest/intro_installation.html
3. Ensure you have the AWS boto library for Python installed (pip install boto boto3)

## Configuration

1. Create an Ansible hosts file in the ```aws/``` folder called ```aws_inventory``` and use the ```aws_inventory.template``` – there you will add any EC2 instances you've created that you can then operate with Ansible

2. Create an external vars file in the ```aws/vars``` folder called ```external_vars.yml``` using the ```external_vars.yml.template``` file as a basis.

Here's an explanation on those vars:

* dag_repo: ```dag_repo: git@github.com:your_organization/airflow_dags.git```

The dag repo is used to pull Airflow DAG's from your repository with Ansible. Fill in the DAG repo's Github repo address here. You don't need this if you don't use the get_dags workbook.

* airflow_db_password: ```airflow_db_password: [your_password]```

The Airflow DB password is what it says it is – used to fill in and use the password when installing Airflows's Postgres DB. Put a long password there using a random password generator.

* airflow_scheduler_instance_id: ```airflow_scheduler_instance_id: i-[asdasdasd]```

The Amazon AWS instance ID for the EC2  instance for the scheduler. This is permanent even if the external IP / DNS name changes.

* subnet_id: ```subnet_id: subnet-[asdasdasd]```

The Amazon AWS subnet ID. Look it up from the AWS console after creating instances. These could be gathered using Ansible EC2 Facts but I haven't implemented that yet.

* airflow_scheduler_aws_region: ```airflow_scheduler_aws_region: us-east-1```

Amazon AWS region (e.g. us-east-1) that the EC2 instance(s) exist on.

* pem_file_name: ```pem_file_name: [pem_file_name].pem```

To connect to these AWS EC2 instances, you need a pem-keyfile. Here's the name of that pemfile. This will give you a nice printout of the ssh command when starting the instance.

* fernet_key: ```fernet_key: [a_secret_token]```

[The Fernet key](https://cryptography.io/en/latest/fernet/) is used for being able to store passwords in the DB.  "Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography." - docs in the link above. So add a random token that will then be used as a token.


## Usage

1. In the repo's directory, run: ```ansible-playbook -i ./aws/ec2.py [playbook_name].yml```

For example, try: ```ansible-playbook -i ./aws/ec2.py ./aws/start_scheduler.yml```
