from detectors.ec2 import scan_ec2
from detectors.ebs import scan_ebs
from detectors.eip import scan_eip
from detectors.snapshots import scan_snapshots
from reports.html_report import generate_html_report
from mail.email_sender import send_email


ec2_data = scan_ec2()

ebs_data = scan_ebs()

eip_data = scan_eip()

snapshot_data = scan_snapshots()


generate_html_report(

    ec2_data,
    ebs_data,
    eip_data,
    snapshot_data

)

send_email()