import boto3


def scan_ec2():

    ec2 = boto3.client("ec2")

    response = ec2.describe_instances()

    ec2_instances = []

    for reservation in response["Reservations"]:

        for instance in reservation["Instances"]:

            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]
            instance_type = instance["InstanceType"]
            availability_zone = instance["Placement"]["AvailabilityZone"]

            name = "N/A"

            for tag in instance.get("Tags", []):

                if tag["Key"] == "Name":
                    name = tag["Value"]
                    break

            ec2_instances.append({

                "name": name,
                "instance_id": instance_id,
                "state": state,
                "instance_type": instance_type,
                "availability_zone": availability_zone

            })

    return ec2_instances