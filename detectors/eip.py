import boto3


def scan_eip():

    ec2 = boto3.client("ec2")

    response = ec2.describe_addresses()

    eips = []

    for address in response["Addresses"]:

        if address.get("InstanceId") is None:

            eips.append({

                "public_ip": address["PublicIp"],
                "allocation_id": address["AllocationId"],
                "saving": 3.60

            })

    return eips