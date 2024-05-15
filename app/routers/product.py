from fastapi import APIRouter, HTTPException, status
from app.schemas import Product
import random
from logging.config import fileConfig
import logging
from app.custom_json_formatter import CustomJsonFormatter

fileConfig('./app/logging_config.ini')

product_router = APIRouter(prefix="/product", tags=["Product"])


def update_handlers_with_custom_formatter(logger_name):
    logger = logging.getLogger(logger_name)
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            handler.setFormatter(CustomJsonFormatter())


update_handlers_with_custom_formatter('auth_logger')
update_handlers_with_custom_formatter('order_logger')
update_handlers_with_custom_formatter('product_logger')


@product_router.post("", status_code=status.HTTP_201_CREATED)
async def add_product(product: Product):
    success = random.choice([True, False])
    logger = logging.getLogger('product_logger')
    if not success:
        failure_cause = random.choice(["Product with same name already exists.", "Server Error", "Unauthorized"])
        logger.error(f"Create Product - Failed to create product for user ID {product.user_id}: {failure_cause}")
        if failure_cause == "Product with same name already exists.":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=failure_cause)
        elif failure_cause == "Server Error":
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=failure_cause)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=failure_cause)

    # Assuming product addition is successful
    product_id = random.randint(1, 1000000)
    logger.info(f"Create Product - Successfully created product {product_id} by user {product.user_id}")
    return {
        "message": "Product added successfully",
        "user_id": product.user_id,
        "product_id": product_id
    }


@product_router.put("/{product_id}", status_code=status.HTTP_200_OK)
async def update_product(product_id: int, product: Product):
    success = random.choice([True, False])
    logger = logging.getLogger('product_logger')
    if not success:
        failure_cause = random.choice(
            ["Product with same name already exists.", "Product not found", "Server Error", "Unauthorized"]
        )
        logger.error(
            f"Update Product - Failed to update product {product_id} for user ID {product.user_id}: {failure_cause}"
        )
        if failure_cause == "Product with same name already exists.":
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=failure_cause)
        elif failure_cause == "Server Error":
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=failure_cause)
        elif failure_cause == "Product not found":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=failure_cause)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=failure_cause)

    logger.info(f"Update Product - Successfully updated product {product_id} by user {product.user_id}")
    return {
        "message": "Product updated successfully",
        "user_id": product.user_id,
        "product_id": product_id
    }


@product_router.get("/{product_id}", status_code=status.HTTP_200_OK)
async def get_product(product_id: int):
    success = random.choice([True, False])
    logger = logging.getLogger('product_logger')
    if not success:
        failure_cause = random.choice(
            ["Product not found", "Server Error"]
        )
        logger.error(
            f"Get Product - Failed to get product {product_id}: {failure_cause}"
        )
        if failure_cause == "Product not found":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=failure_cause)
        elif failure_cause == "Server Error":
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=failure_cause)

    # Assuming product is found
    logger.info(f"Get Product - Successfully retrieved product {product_id}")
    return {
        "product_id": product_id,
        "name": "Example product",
        "description": "Example description",
        "price": random.uniform(1.0, 100.0)
    }


@product_router.delete("/{product_id}", status_code=status.HTTP_200_OK)
async def delete_product(product_id: int, product: Product):
    success = random.choice([True, False])
    logger = logging.getLogger('product_logger')
    if not success:
        failure_cause = random.choice(
            ["Product not Found", "Server Error", "Unauthorized"]
        )
        logger.error(
            f"Delete Product - Failed to delete {product_id} product for user ID {product.user_id}: {failure_cause}")

        if failure_cause == "Server Error":
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=failure_cause)
        elif failure_cause == "Product not Found":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=failure_cause)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=failure_cause)

    logger.info(f"Delete Product - Successfully deleted product {product_id} by user ID {product.user_id}")
    return {
        "message": "Product deleted successfully",
        "user_id": product.user_id,
        "product_id": product_id
    }
