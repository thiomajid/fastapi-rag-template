from pydantic import BaseModel


class UserQuery(BaseModel):
    """
    Defines an input message from the user
    """
    message: str
