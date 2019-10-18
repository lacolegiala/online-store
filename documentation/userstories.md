# User stories

### As a non-registered user...

- I can login and register
- I can view the products listed on the front page

### As a registered user...

- I can log out
- I can browse products on the front page
- I can order products 
- I can review my orders 
- I can change my password

### As an admin...

- I can add new products 
- I can view the product list containing the "Edit" and "Remove" features 
- I can edit the products
- I can delete the products 
- I can do everything that regular users can as well

## User stories' SQL queries

### As a non-registered user...

- I can view the products listed on the front page
```sql
SELECT * FROM product;
```

### As a registered user...

- I can log out
- I can browse products on the front page
```sql
SELECT * FROM product;
```
- I can order products 
```sql
INSERT INTO store_order (user_id) VALUES (1);
INSERT INTO store_order_has_product (order_id, product_id) VALUES (1, 1);
```
- I can review my orders 
```sql
SELECT * FROM store_order
JOIN account ON store_order.id
```
- I can change my password

### As an admin...

- I can add new products 
- I can view the product list containing the "Edit" and "Remove" features 
- I can edit the products
- I can delete the products 
- I can do everything that regular users can as well


