from twilio.rest import Client

ACCOUNT_SID = <INSERT SID>
AUTH_TOKEN = <INSERT AUTH>


class NotificationManager:

    def send_sms(self, message):

        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
            body=f"{message}",
            from_='<INSERT NUMBER>',
            to='<INSERT NUMBER>'
        )
        print(message.status)


