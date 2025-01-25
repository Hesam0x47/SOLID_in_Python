# Without DIP


class EmailService:
    def sendEmail(self, message: str):
        print(f"send email... {message=}")

class NotificationService:
    def __init__(self):
        self.__email_service = EmailService()

    def sendNotification(self, message: str):
        self.__email_service.sendEmail(message)


NotificationService().sendNotification("this is a sample message")
