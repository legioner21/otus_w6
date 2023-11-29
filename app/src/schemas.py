from pydantic import BaseModel


class BaseOrderDto(BaseModel):
    uuid: str
    name: str


class CreateOrderDto(BaseOrderDto):
    pass


class OrderDto(BaseOrderDto):
    id: int

    class Config:
        orm_mode = True
