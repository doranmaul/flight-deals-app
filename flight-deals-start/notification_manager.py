from twilio.rest import Client
import smtplib

ACCOUNT_SID = ""
AUTH_TOKEN = ""

EMAIL_SMTP = "smtp.gmail.com"
USER = ""
PASSWORD = ""


class NotificationManager:

    def send_sms(self, message):

        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
            body=f"{message}",
            from_='',
            to=''
        )
        print(message.status)

    def send_emails(self, message, emails):
        for email in emails:
            with smtplib.SMTP(EMAIL_SMTP, port=587) as connection:
                connection.starttls()
                connection.login(user=USER, password=PASSWORD)
                connection.sendmail(from_addr=USER,
                                    to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8'))

        # message.encode('utf-8') - have to encode emails so the GBP/Pound symbol displays properly






