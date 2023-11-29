from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import models
import schemas


class PreviouslyCreatedOrderException(Exception):
    pass


def create_order(db: Session, order_dto: schemas.CreateOrderDto) -> schemas.OrderDto:
    try:
        db_order = models.Order(
            uuid=order_dto.uuid,
            name=order_dto.name,
        )
        db.add(db_order)
        db.commit()
        db.refresh(db_order)

        return schemas.OrderDto(
            id=db_order.id,
            uuid=db_order.uuid,
            name=db_order.name
        )
    except IntegrityError:
        raise PreviouslyCreatedOrderException