from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas
import service
from db import get_db

order_router = APIRouter()


@order_router.post(
    "/",
    summary="create order",
)
def create_order(
        order_dto: schemas.CreateOrderDto,
        db: Session = Depends(get_db),
):
    """
    Создание заказа:
    """
    try:
        return service.create_order(db, order_dto)
    except service.PreviouslyCreatedOrderException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="order already exists",
        )


api_router = APIRouter()
api_router.include_router(order_router, prefix="/order", tags=["order"])
