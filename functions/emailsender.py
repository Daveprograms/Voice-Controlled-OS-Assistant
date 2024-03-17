import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_whom, subject, content):
    sender_mail = "davidprograms7@gmail.com"
    sender_password = "snjj whtj zdnf pggl"
    receiver_mail = to_whom

    try:
        msg = MIMEMultipart()
        msg['From'] = sender_mail
        msg['To'] = receiver_mail
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_mail, sender_password)
            server.sendmail(sender_mail, receiver_mail, msg.as_string())
            print("Email sent successfully")
    except Exception as e:
        print(f'Error while sending: {e}')

# Example usage:
# to_email = "Davhuss1k@gmail.com"
# email_subject = "Test Email"
# email_content = "This is a test email."
# send_email(to_email, email_subject, email_content)
