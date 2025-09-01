from uuid import UUID, uuid4
from dataclasses import dataclass, field


#This __eq__ and __hash__ implementation is crucial for us. Because Same attributes but different IDs should be considered different entities.
@dataclass
class Entity:
    # Automatically generates a unique UUID for the 'id' field;
    # excluded from the __init__ method, we can not provide uuid
    id: UUID = field(default_factory=uuid4, init=False)
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.id == other.id
    def __hash__(self) -> int:
        return hash(self.id)