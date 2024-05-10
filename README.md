# vendors

This project implements a set of RESTful APIs for managing vendors, purchase orders, and vendor performance evaluation.

## Setup Instructions

1. Clone the Repository:
2. Install Dependencies:
3.  Database Setup:
- Make migrations:
  ```
  python manage.py makemigrations
  ```
- Apply migrations:
  ```
  python manage.py migrate
  ```

4. Run the Development Server:

   
## API Endpoints

- Vendor Endpoints:
- POST `/api/vendors/`: Create a new vendor.
- GET `/api/vendors/`: List all vendors.
- GET `/api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
- PUT `/api/vendors/{vendor_id}/`: Update a vendor's details.
- DELETE `/api/vendors/{vendor_id}/`: Delete a vendor.

- Purchase Order Endpoints:
- POST `/api/purchase_orders/`: Create a purchase order.
- GET `/api/purchase_orders/`: List all purchase orders.
- GET `/api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
- PUT `/api/purchase_orders/{po_id}/`: Update a purchase order.
- DELETE `/api/purchase_orders/{po_id}/`: Delete a purchase order.

- Vendor Performance Endpoint:
- GET `/api/vendors/{vendor_id}/performance`: Retrieve a vendor's performance metrics.

## Usage

1. Creating a Vendor:
- Send a POST request to `/api/vendors/` with the necessary vendor details in the request body.

2. Listing Vendors:
- Send a GET request to `/api/vendors/` to retrieve a list of all vendors.

3. Retrieving Vendor Details:
- Send a GET request to `/api/vendors/{vendor_id}/` to retrieve details of a specific vendor.

4. Updating a Vendor:
- Send a PUT request to `/api/vendors/{vendor_id}/` with the updated vendor details in the request body.

5. Deleting a Vendor:
- Send a DELETE request to `/api/vendors/{vendor_id}/` to delete a vendor.

6. Creating a Purchase Order:
- Send a POST request to `/api/purchase_orders/` with the necessary purchase order details in the request body.

7. Listing Purchase Orders:
- Send a GET request to `/api/purchase_orders/` to retrieve a list of all purchase orders.

8. Retrieving Purchase Order Details:
- Send a GET request to `/api/purchase_orders/{po_id}/` to retrieve details of a specific purchase order.

9. Updating a Purchase Order:
- Send a PUT request to `/api/purchase_orders/{po_id}/` with the updated purchase order details in the request body.

10. Deleting a Purchase Order:
 - Send a DELETE request to `/api/purchase_orders/{po_id}/` to delete a purchase order.

11. Retrieving Vendor Performance Metrics:
 - Send a GET request to `/api/vendors/{vendor_id}/performance` to retrieve the calculated performance metrics for a specific vendor.

## Test Suite

The test suite includes comprehensive tests for all API endpoints to ensure functionality and reliability.

To run the tests:

## Contributors

- [Contributor 1](https://github.com/mudasirmattoo)


## License

This project is licensed under the [MIT License](LICENSE).


