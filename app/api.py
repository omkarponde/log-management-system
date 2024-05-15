import logging
import os

import uvicorn
from fastapi import FastAPI
from app.routers import auth_router, order_router, product_router, log_router


app = FastAPI()
# Include the auth router
app.include_router(auth_router)
app.include_router(order_router)
app.include_router(product_router)
app.include_router(log_router)


def create_log_directory():
    current_dir = os.path.dirname(__file__)
    log_dir = os.path.join(current_dir, "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        for dir in ['auth', 'order', 'product']:
            dir_path = os.path.join(log_dir, dir)
            os.makedirs(dir_path)
            for filename in ['app.log', 'error.log']:
                filepath = os.path.join(dir_path, filename)
                if not os.path.exists(filepath):
                    open(filepath, 'a').close()
        print(f"Created log directory: {log_dir}")
    else:
        print(f"Log directory already exists: {log_dir}")

@app.get("/")
async def read_root():
    create_log_directory()

    return {"message": "Hello, FastAPI!!!"}

if __name__ == "__main__":
    try:
        create_log_directory()
    except:
        print("exception occured")
#     # import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    # port = int(os.getenv("PORT", 8000))
    # uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)

