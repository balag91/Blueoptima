import boto3
import csv

# My AWS credentials
aws_access_key_id = 'XXXXXXXXXXXX'
aws_secret_access_key = 'XXXXXXXXXXXXX'
region_name = 'us-east-1'

ec2_client = boto3.client('ec2', region_name=region_name)

def update_instance_tags(instance_id, new_department):
    ec2_client.create_tags(
        Resources=[instance_id],
        Tags=[{'Key': 'Department', 'Value': new_department}]
    )
    print(f"Updated Department tag of instance {instance_id} to '{new_department}'")

# Reading CSV file
csv_file = 'tag_changes.csv'

with open(csv_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        hostname = row['Hostname']
        old_department = row['Current Department']
        new_department = row['New Department']

        # Filter instance by hostname and department
        response = ec2_client.describe_instances(
            Filters=[
                {'Name': 'tag:Hostname', 'Values': [hostname]},
                {'Name': 'tag:Department', 'Values': [old_department]}
            ]
        )

        # updating tags on matching instance
        for taginstance in response['Reservations']:
            for instance in taginstance['Instances']:
                instance_id = instance['InstanceId']
                update_instance_tags(instance_id, new_department)