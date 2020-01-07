import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '21d2864a00941e'
    password = 'aa79761d8bba6a'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = "test@example.com"
    receiver_email = "test2@example.com"
    # allow us to send text in HTML emails
    msg = MIMEText(message, "html")
    msg["Subject"] = "Tesla Feedback"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Send email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login,password)
        server.sendmail(sender_email, receiver_email, msg.as_string())