from dataclasses import dataclass

# without @dataclass
class Order:
    def __init__(self, id, customer_id, total_amount):
        self.id = id
        self.customer_id = customer_id
        self.total_amount = total_amount

    def __repr__(self):
        return f"Order(id={self.id}, customer_id={self.customer_id}, total_amount={self.total_amount})"
    
@dataclass
class Order:
    id : str
    customer_id : str
    total_amount : float
# __init__ is created for you.
# __repr__ is created for you.
# __eq__ (equality check) is created for you.
# You can still add methods if needed.
# Think of @dataclass as Python’s way of giving you “auto-generated constructors and helpers” for simple data-holding classes.


