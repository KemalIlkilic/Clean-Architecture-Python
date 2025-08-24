from typing import Protocol

#It defines a structural subtyping interface rather than requiring explicit inheritance.
class Notifier(Protocol):
    def send_notifications(self, message : str) -> None:
        pass

class EmailNotifier: # Note: no explicit inheritance
    def send_notification(self, message: str) -> None:
        print(f"Sending email: {message}")
class SMSNotifier: # Note: no explicit inheritance
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS: {message}")
        
class NotificationService:
# Still able to use type hinting
    def __init__(self, notifier: Notifier):
        self.notifier = notifier
    def notify(self, message: str) -> None:
        self.notifier.send_notification(message)
# Usage
sms_notifier = SMSNotifier()
sms_service = NotificationService(sms_notifier)
sms_service.notify("Hello via SMS")

"""
Protocol versus ABC: The Notifier class is now a Protocol class instead of an ABC class. It defines a structural subtyping interface rather than requiring explicit inheritance.
Implicit conformance: The EmailNotifier and SMSNotifier classes dont explicitly inherit from the Notifier class, but they conform to its interface by implementing the send_notification method.

Duck typing with type hinting: This approach combines Python's duck typing flexibility with the benefits of static type checking, aligning with Clean Architecture's emphasis on loose coupling.
Concrete implementations: The NotificationService class still depends on the abstract Notifier protocol, not concrete implementations, adhering to Clean Architecture principles.
"""