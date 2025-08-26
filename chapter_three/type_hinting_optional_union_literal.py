from typing import Union, Optional, Literal

def process_input(data: Union[str, int]) -> str:
    return str(data)

def find_user(user_id: Optional[int] = None) -> Optional[str]:
    if user_id is None:
        return None
    return "User found"

def process_input_python(data: str | int) -> str:
    return str(data)

def find_user_python(user_id: int | None = None) -> str | None:
    if user_id is None:
        return None
    return "User found"

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]

def set_log_level(level : LogLevel):
    print(f"Setting log level to {level}")