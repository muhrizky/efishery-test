# Project Efishery Test

## Overview

This project includes several modules for user management, authentication, data fetching, and marketplace transactions. The project is built on Odoo 14 Community Edition and integrates various functionalities to enhance user experience and system capabilities.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [User Module](#user-module)
  - [Auth Module](#auth-module)
  - [Fetch Module](#fetch-module)
  - [Marketplace Module](#marketplace-module)
- [API Documentation](#apidoc)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/muhrizky/efishery-test.git
   cd project-name
   ```
   **Alternative**:
extract the contents from the archive file.

2.  **Set up Odoo**
Follow Odoo's official documentation to install and configure Odoo.
Ensure that Odoo is properly set up and running before proceeding.
   
## Usage

### User Module

#### Short Description

The User Module utilizes OCA's Queue Job and Base Import Async modules. It streamlines bulk user creation, processing hundreds or more users seamlessly in the background without user intervention. Users can track progress and opt for notifications upon completion. This feature seamlessly integrates into Odoo's data import flow, introducing a new checkbox for deferred background job processing. For more details, consult the README documentation within the module, outlining the enhanced import workflow.

#### Key Features

* Batch user import
* Background process
* Process status monitoring

#### Demo
[Watch the demo video](https://www.loom.com/share/1e95b44348cb4a58a8ac16dffacca4b1?sid=4b3eff82-bf1a-4caf-a748-a268233ece55)

### Auth Module

#### Short Description

The Auth Module provides user authentication through a single login endpoint. This endpoint returns a JWT token containing private claims such as the user's email and role. The module also has the ability to limit active logins to only one browser tab/device (nice to have feature).

#### Key Features

* Single login endpoint with JWT token
* Active login limit per user 
* Single logout endpoint with JWT token

#### Demo
[Watch the demo video](https://www.loom.com/share/2f7241f058f443959ac832d07d710999?sid=efca11d3-a99f-482e-b109-fa5902fe1f98)

### Fetch Module

#### Short Description

The Fetch Module allows users to retrieve data from external resources. The module provides an endpoint to fetch data from this
[resource]( https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab)
Additional features include:

* Adding a new price field in USD (converted from IDR) using a currency converter [service](https://freecurrencyapi.com/) 
* Caching to improve request performance
* Handling invalid JWT tokens

#### Key Features

* Fetch endpoint from external resource
* IDR to USD currency conversion
* Caching for request performance
* Invalid JWT token handling

#### Demo
[Watch the demo video](https://www.loom.com/share/0a74ece725b04318959af3a3c9d2af42?sid=99ad633d-6ff6-41c4-bf44-6989d2c08d17)

### Marketplace Module

#### Short Description

The Marketplace Module provides functionality for order transactions up to payment. The module creates a sale order with a confirmed state, an invoice with a posted state, and a payment registered with an invoice in payment status.

#### Key Features

* Endpoint for order transactions up to payment
* Endpoint to fetch sale order list
* Invalid JWT token handling
#### Demo
[Watch the demo video](https://www.loom.com/share/1c8da9d5d9c24f04be3a148d13ef7882?sid=1a3ad476-8317-490d-bccc-de775eee94ec)

## API Documentation
This API allows you to manage data efficiently.
The Postman collection is included in this repository for your convenience; you can check the file `efishery_test.postman_collection.json`. For detailed online documentation and API endpoints, please visit the [eFishery Skill Test API Collection on Postman](https://documenter.getpostman.com/view/10909317/2sA3QzbUrF#2e5bfdee-6626-415b-b63f-2fed74753d67).

### Notes
* Complete documentation and usage guides will be provided later.
* Please contact [LinkedIn](https://www.linkedin.com/in/muhrizqi/) or [Email](muhrizqi.work@gmail.com) for any questions or issues.

### Version

* 1.0.0 (2024-05-25): Initial release.
