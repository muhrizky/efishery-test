# README C4 Diagram Documentation

## System Overview
This documentation provides an overview of the system, including its modules and deployment architecture. The system consists of the following modules: User Module, Auth Module, Fetch Module, and Marketplace Module.

## Context Diagram

``` sql
+------------------+    +------------------+    +------------------+    +------------------+
|    User Module   |    |   Auth Module    |    |   Fetch Module   |    | Marketplace      |
|                  |    |                  |    |                  |    | Module           |
|                  |    |                  |    |                  |    |                  |
|   Initiates      |    |    Initiates     |    |    Initiates     |    | Initiates        |
|   User Import    |    |    User Login    |    |    Data Fetch    |    | Order & Payment  |
|   Processes      |    |    Processes     |    |    Processes     |    | Creation         |
+------------------+    +------------------+    +------------------+    +------------------+
```

## Deployment Diagram
``` sql
+----------------------+    +----------------------+    +----------------------+    +----------------------+
|       User Module    |    |      Auth Module     |    |      Fetch Module    |    |   Marketplace        |
|      (Application)   |    |     (Application)    |    |     (Application)    |    |    Module            |
+----------------------+    +----------------------+    +----------------------+    +----------------------+
            |                        |                          |                          |       
            |                        |                          |                          |      
+-----------|------------------------|--------------------------|--------------------------|----------------------+
|           v                        v                          v                          v                      |
|       +------------------+    +------------------+    +------------------+    +------------------+         |
|       |     Database     |    |     Database     |    |    External      |    |     Database      |         |
|       |      Server      |    |      Server      |    |    Resource     |    |      Server        |         |
|       +------------------+    +------------------+    +------------------+    +------------------+         |
|               |                        |                          |                          |                  |
|               |                        |                          |                          |                  |
|       +------------------+    +------------------+    +------------------+    +------------------+         |
|       |  Background      |    |  JWT Token       |    |  Currency        |    |   Order & Payment |         |
|       |  Process         |    |  Generation      |    |  Converter API   |    |   Management      |         |
|       |  Handler         |    +------------------+    +------------------+    +------------------+         |
|       +------------------+                                                                              |
|                                                                                                          |
+----------------------------------------------------------------------------------------------------------+
```

## Module Details

### User Module
**User Import:**
- **Initiator:** System Administrator
- **Action:** Initiate user import process
- **Input:** CSV file containing user data
- **Output:** None
- **Process:**
  - System validates CSV file format and content.
  - System imports user data into the database.

**Background Process:**
- **Initiator:** User Import component
- **Action:** Handle user import process in the background
- **Input:** User data from CSV file
- **Output:** None
- **Process:**
  - System iterates through user data and creates user records in the database.
  - System handles any errors or exceptions during the import process.

### Auth Module
**Login & JWT Generation:**
- **Initiator:** User
- **Action:** Login to the system
- **Input:** Username and password
- **Output:** JWT token
- **Process:**
  - System authenticates user credentials against the database.
  - System generates a JWT token containing user claims (email, role).
  - System returns the JWT token to the user.

**Single Session Management:**
- **Initiator:** System
- **Action:** Manage user sessions
- **Input:** JWT token
- **Output:** None
- **Process:**
  - System validates JWT token and retrieves user session information.
  - System invalidates all other sessions for the same user.
  - System updates the current session expiration time.

### Fetch Module
**Data Fetching & Currency Conversion:**
- **Initiator:** User
- **Action:** Fetch data from an external resource
- **Input:** URL of the external resource
- **Output:** Data with converted currency values
- **Process:**
  - System makes an HTTP request to the external resource URL.
  - System parses the JSON response and extracts relevant data.
  - System converts currency values from IDR to USD using a currency converter API.

**Error Handling & Validation:**
- **Initiator:** System
- **Action:** Handle errors and validate data
- **Input:** User request, external resource data
- **Output:** Error message or validated data
- **Process:**
  - System validates the user's JWT token and authorization.
  - System checks for errors in the external resource response.
  - If errors are found, return an appropriate error message.

### Marketplace Module
**Order & Payment Creation:**
- **Initiator:** User
- **Action:** Create a new order and payment
- **Input:** Order details, payment information
- **Output:** Order ID and payment confirmation
- **Process:**
  - System validates the order details and payment information.
  - System creates a new sale order record in the database with state 'confirmed'.

## Relationships and Data Flow

### Relationships:
- **User -> Web Application:** User interacts with the system through the web application.
- **Web Application -> (Order & Payment, Sale Order Management):** Web application forwards user requests to relevant components.
- **Order & Payment -> Database (Primary):** Writes order, invoice, and payment data to the primary database.
- **Sale Order Management -> Database (Primary/Slave):** Reads sale order data from the primary or slave database.

### Data Flow:
- **User initiates order:** User submits order details and payment information through the web application.
- **Web application validates and processes:**
  - Web application validates user credentials and order data.
  - If JWT token is invalid, return an error message.
  - Otherwise, forwards data to the Order & Payment component.
- **Order & Payment creates records:**
  - Order & Payment component creates a sale order (confirmed state), invoice (posted state), and registers payment (invoice in payment).
  - If any error occurs, return an error message.
- **Web application returns confirmation:** Web application returns order ID and payment confirmation to the user.
- **User fetches sale orders:** User requests a list of sale orders.
- **Web application validates and retrieves:**
  - Web application validates user credentials.
  - If JWT token is invalid, return an error message.
- **Web application displays list:** Web application displays a list of sale orders with relevant details to the user.

This documentation provides a high-level overview of the system architecture and workflows. For detailed technical implementation, please refer to the respective module documentation and code comments.




