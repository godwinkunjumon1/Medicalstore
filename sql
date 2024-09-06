CREATE DATABASE medical_store;
USE medical_store;
CREATE TABLE medicines (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    brand VARCHAR(100),
    price DECIMAL(10, 2),
    quantity INT
);
CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    contact VARCHAR(15),
    address TEXT
);
CREATE TABLE sales (
    id INT PRIMARY KEY AUTO_INCREMENT,
    medicine_id INT,
    customer_id INT,
    quantity_sold INT,
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (medicine_id) REFERENCES medicines(id),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
