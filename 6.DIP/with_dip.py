from abc import ABC, abstractmethod


# With DIP
class AbstractNotificationSender(ABC):
    @abstractmethod
    def send(self, message: str):
        raise NotImplementedError


class EmailSender(AbstractNotificationSender):
    def send(self, message: str):
        print(f"send email... {message=}")


class NotificationService:
    def __init__(self, notification_sender: AbstractNotificationSender):
        self.__notification_sender = notification_sender

    def sendNotification(self, message: str):
        self.__notification_sender.send(message)


# The magic is here! If tomorrow we decide to send messages using SMS, 
# we will implement a new class named SMSSender and replace it with the following line
notification_sender = EmailSender()
NotificationService(notification_sender=notification_sender).sendNotification("this is a sample message")
