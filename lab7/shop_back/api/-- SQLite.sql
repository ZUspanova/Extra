-- SQLite
INSERT INTO api_product (name, price, description, quantity, category_id, is_active)
VALUES ('iPhone 15 Pro Max', 700000.00, 'Iphone 15 Pro Max description', 3, 1, True),
       ('Samsung Galaxy S21', 650000.00, 'Samsung Galaxy S21 description', 5, 2, True),
       ('OnePlus 8', 500000.00, 'OnePlus 8 description', 4, 3, False),
       ('Google Pixel 6', 550000.00, 'Google Pixel 6 description', 2, 4, False);

SELECT id, name, price, description, quantity FROM api_product WHERE is_active=True;