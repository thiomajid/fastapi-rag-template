import datetime

from pydantic import BaseModel


class UserQuery(BaseModel):
    """
    Defines an input message from the user
    """

    conversationId: int
    message: str
    sentDateTime: datetime.datetime


class LmResponse(BaseModel):
    """
    The generated answer by the LLM using the query index
    """

    message: str
    sentDateTime: datetime.datetime
