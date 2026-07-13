import boto3


def scan_ebs():

    ec2 = boto3.client("ec2")

    response = ec2.describe_volumes()

    volumes = []

    for volume in response["Volumes"]:

        if len(volume["Attachments"]) == 0:

            saving = volume["Size"] * 0.08

            volumes.append({

                "volume_id": volume["VolumeId"],
                "size": volume["Size"],
                "state": volume["State"],
                "availability_zone": volume["AvailabilityZone"],
                "saving": saving

            })

    return volumes