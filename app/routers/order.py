from fastapi import APIRouter, HTTPException, status
from app.schemas import Order
import random
from app.logger_config import get_logger


# Create an instance of APIRouter
order_router = APIRouter(
    prefix="/order",
    tags=["Order"],
)


@order_router.post("", status_code=status.HTTP_201_CREATED)
async def create_order(order: Order):
    success = random.choice([True, False])
    logger = get_logger('order_logger')
    if not success:
        failure_cause = random.choice(["Item not available", "Server Error", "Unauthorized"])
        logger.error(f"Create Order - Failed to create order by user ID {order.user_id}: {failure_cause}")
        if failure_cause == "Item not available":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=failure_cause)
        elif failure_cause == "Server Error":
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=failure_cause)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=failure_cause)

    order_id = random.randint(1, 1000000)
    logger.info(f"Create Order - Order {order_id} created successfully for user ID {order.user_id}")
    return {
        "message": "Order created successfully",
        "order_id": order_id,
        "created_by_user_id": order.user_id
    }


@order_router.get("/{order_id}", status_code=status.HTTP_200_OK)
async def get_order(order_id: int):
    success = random.choice([True, False])
    logger = get_logger('order_logger')
    if not success:
        failure_cause = random.choice(["Order not found", "Server Error"])
        logger.error(
            f"Get Order - Failed to get order {order_id}: {failure_cause}")
        if failure_cause == "Order not found":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=failure_cause)
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=failure_cause)

    # Assuming order is found
    logger.info(f"Get Order - Successfully retrieved order {order_id}")
    return {"order_id": order_id, "item": "Example item", "quantity": random.randint(1, 10)}


# Define the update order endpoint
@order_router.put("/{order_id}", status_code=status.HTTP_200_OK)
async def update_order(order_id: int, order: Order):
    success = random.choice([True, False])
    logger = get_logger('order_logger')
    if not success:
        failure_cause = random.choice(["Order not found", "Server Error", "Unauthorized"])
        logger.error(
            f"Update Order - Failed to update order {order.order_id} by user ID {order.user_id}: {failure_cause}")
        if failure_cause == "Order not found":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=failure_cause)
        elif failure_cause == "Server Error":
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=failure_cause)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=failure_cause)

    logger.info(f"Update Order - Successfully updated order {order_id} by user ID {order.user_id}.")
    # Assuming order update is successful
    return {
        "user_id": order.user_id,
        "message": "Order updated successfully",
        "order_id": order_id
    }


@order_router.delete("/{order_id}", status_code=status.HTTP_200_OK)
async def delete_order(order_id: int, order: Order):
    success = random.choice([True, False])
    logger = get_logger('order_logger')
    if not success:
        failure_cause = random.choice(["Order not found", "Server Error", "Unauthorized"])
        logger.error(
            f"Delete Order - Failed to delete order {order.order_id} by user ID {order.user_id}: {failure_cause}")
        if failure_cause == "Order not found":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=failure_cause)
        elif failure_cause == "Server Error":
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=failure_cause)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=failure_cause)

    # Assuming order deletion is successful
    logger.info(f"Delete Order - Successfully deleted order {order_id}")
    return {
        "message": "Order deleted successfully",
        "user_id": order.user_id,
        "order_id": order_id
    }
