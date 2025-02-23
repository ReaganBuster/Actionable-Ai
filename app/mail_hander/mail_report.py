import smtplib

class MailReport:
    def __init__(self, sender, receiver, sender_credentials, body, subject) -> None:
        self.sender = sender
        self.receiver = receiver
        self.sender_credentials = sender_credentials
        self.body = body
        self.subject = subject
        
    def send_report(self):
        try:
            message = f"Subject: {self.subject}\n\n{self.body}"
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.sender, self.sender_credentials)
                server.sendmail(self.sender, self.receiver, message)
            print("Email sent successfully!")
        except smtplib.SMTPAuthenticationError as e:
            print("Authentication error: Please use an application-specific password.")
            print(f"Error details: {e}")
        except Exception as e:
            print(f"Error sending email: {e}")