from abc import ABC, abstractmethod
#Example of Clean Architecture Dependency Inversion Principle

#Interface, represents our core business rules
class Notifier(ABC):
    @abstractmethod
    def send_notifications(self, message : str) -> None:
        pass

#Concrete Class
class EmailNotifier(Notifier):
    def send_notifications(self, message : str) -> None:
        print(f"Sending email: {message}")

#Concrete Class
class SMSNotifier(Notifier):
    def send_notifications(self, message: str) -> None:
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier
    def notify(self, message: str) -> None:
        self.notifier.send_notifications(message)
# Usage

email_notifier = EmailNotifier()
email_service = NotificationService(email_notifier)
email_service.notify("Hello via email")
