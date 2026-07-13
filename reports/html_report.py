from datetime import datetime


def generate_html_report(ec2, ebs, eips, snapshots):

    total = 0

    html = f"""
    <html>

    <head>

    <title>AWS Cost Optimization Report</title>

    <style>

    body{{font-family:Arial;margin:40px;}}

    table{{border-collapse:collapse;width:100%;margin-bottom:25px;}}

    th,td{{border:1px solid black;padding:8px;text-align:left;}}

    h2{{background:#eeeeee;padding:8px;}}

    </style>

    </head>

    <body>

    <h1>AWS Cost Optimization Report</h1>

    <p>Generated : {datetime.now()}</p>

    """

    # ---------------- EC2 ----------------

    html += "<h2>EC2 Instances</h2>"

    html += """
    <table>

    <tr>

    <th>Name</th>
    <th>ID</th>
    <th>State</th>
    <th>Type</th>

    </tr>
    """

    for instance in ec2:

        html += f"""
        <tr>

        <td>{instance["name"]}</td>

        <td>{instance["instance_id"]}</td>

        <td>{instance["state"]}</td>

        <td>{instance["instance_type"]}</td>

        </tr>
        """

    html += "</table>"

    # ---------------- EBS ----------------

    html += "<h2>Unused EBS Volumes</h2>"

    html += """
    <table>

    <tr>

    <th>Volume ID</th>

    <th>Size (GB)</th>

    <th>Saving ($)</th>

    </tr>
    """

    for volume in ebs:

        total += volume["saving"]

        html += f"""
        <tr>

        <td>{volume["volume_id"]}</td>

        <td>{volume["size"]}</td>

        <td>{volume["saving"]:.2f}</td>

        </tr>
        """

    html += "</table>"

    # ---------------- Elastic IP ----------------

    html += "<h2>Unused Elastic IP</h2>"

    html += """
    <table>

    <tr>

    <th>Public IP</th>

    <th>Saving ($)</th>

    </tr>
    """

    for ip in eips:

        total += ip["saving"]

        html += f"""
        <tr>

        <td>{ip["public_ip"]}</td>

        <td>{ip["saving"]:.2f}</td>

        </tr>
        """

    html += "</table>"

    # ---------------- Snapshots ----------------

    html += "<h2>Old Snapshots</h2>"

    html += """
    <table>

    <tr>

    <th>Snapshot</th>

    <th>Age</th>

    <th>Saving ($)</th>

    </tr>
    """

    for snap in snapshots:

        total += snap["saving"]

        html += f"""
        <tr>

        <td>{snap["snapshot_id"]}</td>

        <td>{snap["age"]} Days</td>

        <td>{snap["saving"]:.2f}</td>

        </tr>
        """

    html += "</table>"

    html += f"<h2>Total Potential Saving : ${total:.2f}/month</h2>"

    html += """

    </body>

    </html>

    """

    with open("reports/report.html", "w", encoding="utf-8") as file:

        file.write(html)

    print("HTML Report Generated Successfully!")