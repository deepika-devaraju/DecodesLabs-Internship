-- Project 3: SQL Data Analysis - Sales Insights
-- Database: SQLite
-- Import sales_data.csv into a table named sales before running these queries.
-- In DB Browser for SQLite: File > Import > Table from CSV file.

-- 1. Display all records
SELECT * FROM sales;

-- 2. Select specific columns
SELECT customer_name, product, quantity, price
FROM sales;

-- 3. Filter sales from Bengaluru
SELECT *
FROM sales
WHERE city = 'Bengaluru';

-- 4. Find sales with a product price above 10,000
SELECT *
FROM sales
WHERE price > 10000;

-- 5. Sort records by price (highest first)
SELECT *
FROM sales
ORDER BY price DESC;

-- 6. Sort records by sale date (oldest first)
SELECT *
FROM sales
ORDER BY sale_date ASC;

-- 7. Count the total number of sales records
SELECT COUNT(*) AS total_sales
FROM sales;

-- 8. Calculate total quantity sold
SELECT SUM(quantity) AS total_quantity_sold
FROM sales;

-- 9. Calculate the average product price
SELECT ROUND(AVG(price), 2) AS average_product_price
FROM sales;

-- 10. Calculate total revenue
SELECT SUM(quantity * price) AS total_revenue
FROM sales;

-- 11. Count sales by product category
SELECT category, COUNT(*) AS number_of_sales
FROM sales
GROUP BY category
ORDER BY number_of_sales DESC;

-- 12. Calculate revenue by category
SELECT category,
       SUM(quantity * price) AS category_revenue
FROM sales
GROUP BY category
ORDER BY category_revenue DESC;

-- 13. Calculate revenue by city
SELECT city,
       SUM(quantity * price) AS city_revenue
FROM sales
GROUP BY city
ORDER BY city_revenue DESC;

-- 14. Find total quantity sold for each product
SELECT product,
       SUM(quantity) AS quantity_sold
FROM sales
GROUP BY product
ORDER BY quantity_sold DESC;

-- 15. Show categories with more than 3 sales records
SELECT category, COUNT(*) AS number_of_sales
FROM sales
GROUP BY category
HAVING COUNT(*) > 3
ORDER BY number_of_sales DESC;
