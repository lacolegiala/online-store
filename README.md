# Online store 

A cosmetics online store selling different cosmetics products. The product list lists the name and the price of every product. One product can be in many orders, and one order can have multiple products.

After logging in, the user can both browse and order the products. The products can be ordered by selecting the desired products and pressing "Add to order" button. 

## Features

- Logging in and registering
- Browsing products
- Ordering products
- Reviewing orders
- Adding products (admin)
- Deleting and editing products (admin)

## ⚠️ Known bugs

The delete feature doesn't work in the production! So please don't remove products or accounts until it's fixed. This will be fixed in the near future.


## Demo

A link to the production:

https://lacolegiala-online-store.herokuapp.com

The username for admin is "admin" and the password is "1234567890"

## Database schema

![A database schema that contains tables for User, Product, Order and Role](Online-store-database-schema.png)

CREATE TABLE statements:


```sql
CREATE TABLE role (
	id INTEGER NOT NULL,
	name VARCHAR(80),
	PRIMARY KEY (id), 
	UNIQUE (name)
);
```

```sql
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	active BOOLEAN, 
	PRIMARY KEY (id), 
	CHECK (active IN (0, 1))
);
```

```sql
CREATE TABLE product (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	price INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
```
```sql
CREATE TABLE roles_users (
	user_id INTEGER, 
	role_id INTEGER, 
	FOREIGN KEY(user_id) REFERENCES account (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
);
```

```sql
CREATE TABLE store_order (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES account (id)
);
```

```sql
CREATE TABLE store_order_has_product (
	store_order_id INTEGER NOT NULL, 
	product_id INTEGER NOT NULL, 
	PRIMARY KEY (store_order_id, product_id), 
	FOREIGN KEY(store_order_id) REFERENCES store_order (id), 
	FOREIGN KEY(product_id) REFERENCES product (id)
)
```

## Details

### How to use

The application works by going to the address linked under title "Demo". 

#### As a non-registered user...

- I can login and register
- I can view the products listed on the front page

#### As a user...

- I can log out
- I can browse products on the front page
- I can order products 
- I can review my orders 

#### As an admin...

- I can add new products 
- I can view the product list containing the "Edit" and "Remove" features 
- I can edit the products
- I can delete the products
- I can do everything that regular users can as well

### Installing the app

First, create Python virtual environment.

`python3 -m venv venv`

Next, activate it.

`source venv/bin/activate`

Install dependencies.

`pip install -r requirements.txt`

If you face this error when installing dependencies

`ld: library not found for -lssl`

try this:

```bash
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
```
Then try to install dependencies again.



