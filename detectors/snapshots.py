import boto3
from datetime import datetime


def scan_snapshots():

    ec2 = boto3.client("ec2")

    response = ec2.describe_snapshots(
        OwnerIds=["self"]
    )

    snapshots = []

    for snapshot in response["Snapshots"]:

        today = datetime.now(snapshot["StartTime"].tzinfo)

        age = (today - snapshot["StartTime"]).days

        if age > 0 or age == 0:
            

            saving = snapshot["VolumeSize"] * 0.05

            snapshots.append({

                "snapshot_id": snapshot["SnapshotId"],
                "volume_size": snapshot["VolumeSize"],
                "age": age,
                "state": snapshot["State"],
                "saving": saving

            })

    return snapshots