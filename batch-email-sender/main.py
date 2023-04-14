import argparse
import smtplib
from email.mime.text import MIMEText

parser = argparse.ArgumentParser(description="Batch email sender parameters")
parser.add_argument("--smtp-server-host", "-s", dest="smtp_server_host", help="SMTP server host")
parser.add_argument("--smtp-server-port", "-p", dest="smtp_server_port", help="SMTP server port")
parser.add_argument("--sender-email", "-se", dest="sender_email", help="Sender email address")
parser.add_argument("--sender-password", "-sp", dest="sender_password", help="Sender password")
parser.add_argument("--email-subject", "-es", dest="email_subject", help="Email subject")
parser.add_argument("--email-body", "-eb", dest="email_body",
                    help="Email body (support multi-line)")
parser.add_argument("--email-list", "-f", dest="email_list",
                    help="Absolute path for the email address list (one per line)")

args = parser.parse_args()

# SMTP server configuration
smtp_server_host = args.smtp_server_host
smtp_server_host_port = args.smtp_server_port
sender_email = args.sender_email
sender_password = args.sender_password

# Email content
email_subject = args.email_subject
email_body = args.email_body
email_list = args.email_list


def main():
    with open(email_list, "r") as file:
        email_file = file.readlines()

    with open(email_body, "r") as file:
        body = file.read()

    for recipient in email_file:
        msg = MIMEText(body)
        msg['Subject'] = email_subject
        msg['From'] = sender_email
        msg['To'] = recipient
        smtp_server = smtplib.SMTP_SSL(smtp_server_host, smtp_server_host_port)
        smtp_server.login(sender_email, sender_password)
        smtp_server.sendmail(sender_email, recipient, msg.as_string())
        smtp_server.quit()
        print("Successfully sent the email to", recipient)


if __name__ == "__main__":
    main()
