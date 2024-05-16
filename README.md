# Log Ingestor

Log Ingestor is a Python application built using FAST API that implements a logging system and exposes APIs to generate random success or failure responses.

## Features

- **Logging System**: Implemented a logging system to capture activity within the application.
- **APIs**: Exposes APIs to generate random success or failure responses for testing purposes.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/omkarponde/log-management-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd log-management-system
    ```

3. (Optional but recommended) Create and activate a virtual environment:
   
    - **For Windows**:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

    - **For macOS and Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the application:

    ```bash
    uvicorn app.api:app --reload
    ```

2. Access the APIs using the following endpoints:
    To explore and interact with the APIs using Swagger UI, navigate to [http://localhost:8000/docs](http://localhost:8000/docs) in your web browser.

## Logging

The logging system captures activity from the APIs and writes logs to a designated file. The logs of three services are recorded:

1. **Auth**: Logs related to authentication activities.
2. **Order**: Logs related to order processing activities.
3. **Product**: Logs related to product management activities.

These logs are stored in the following directory structure:
    - `./app/tmp/logs/auth/app.log`
    - `./app/tmp/logs/auth/error.log`
    - `./app/tmp/logs/product/app.log`
    - `./app/tmp/logs/product/error.log`
    - `./app/tmp/logs/order/app.log`
    - `./app/tmp/logs/order/error.log`
## Example Log Entry

Here's an example of a log entry in the specified format:

```json
{
    "level": "error",
    "log_string": "Delete Order - Failed to delete order 0 by user ID 0: Unauthorized",
    "timestamp": "2023-09-15T08:00:00Z",
    "metadata": {
        "source": "./app/tmp/logs/order/error.log"
    }
}
```

### Log Filtering in Swagger UI

You can filter logs in the Swagger UI based on the following criteria:

1. **Level**: Filter logs by severity level, which can be "info" or "error".
2. **Log String**: Enter keywords like "Success" to see success logs, "Failed" to see failure logs, "Create", Update, Delete or "Get" to see specific logs. You can also use "Product" or "Order" to search fot the logs realted to those services. Note: This is case sensitive input field. Example: Use "Update Order" and you will get all the logs regarding update order.
3. **Time Range**: Specify a start time and end time in the format `YYYY-MM-DDTHH:MM:SSZ` to filter logs within a specific time range.
4. **Source**: Choose the source log file from the following options:
    - `./app/tmp/logs/auth/app.log`
    - `./app/tmp/logs/auth/error.log`
    - `./app/tmp/logs/product/app.log`
    - `./app/tmp/logs/product/error.log`
    - `./app/tmp/logs/order/app.log`
    - `./app/tmp/logs/order/error.log`

Ensure to enter the time range in the specified format for accurate filtering.
 The hosted URL of the project -> https://log-management-system-899428d80083.herokuapp.com/docs
