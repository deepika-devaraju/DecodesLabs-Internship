# SQL Data Analysis – Sales Insights

## Project Overview
This beginner-friendly project uses SQL to analyze a sample sales dataset and discover useful business insights. It demonstrates data retrieval, filtering, sorting, grouping, and basic aggregations.

## Objectives
- Retrieve records using `SELECT`.
- Filter records using `WHERE`.
- Sort results using `ORDER BY`.
- Group data using `GROUP BY`.
- Summarize data using `COUNT()`, `SUM()`, and `AVG()`.
- Calculate sales revenue using `quantity * price`.

## Files in This Repository
| File | Description |
|---|---|
| `sales_data.csv` | Demo sales dataset with 20 sample records |
| `queries.sql` | 15 SQL queries covering the project requirements |
| `README.md` | Project documentation and setup instructions |

## Dataset Description
The CSV contains the following columns:

| Column | Description |
|---|---|
| `sale_id` | Unique ID for each sale |
| `customer_name` | Customer name |
| `product` | Product sold |
| `category` | Product category |
| `quantity` | Number of units sold |
| `price` | Price per unit |
| `sale_date` | Date of sale (`YYYY-MM-DD`) |
| `city` | Customer's city |

The data is fictional and is provided for learning and demonstration purposes only.

## Tools Required
- SQLite
- DB Browser for SQLite (recommended for beginners), or another SQLite client
- Git and GitHub (to publish the project)

## How to Run the Project

### Option 1: DB Browser for SQLite
1. Install and open **DB Browser for SQLite**.
2. Select **New Database** and save it as `sales_analysis.db`.
3. Open the **Execute SQL** tab and run:

   ```sql
   CREATE TABLE sales (
       sale_id INTEGER PRIMARY KEY,
       customer_name TEXT,
       product TEXT,
       category TEXT,
       quantity INTEGER,
       price REAL,
       sale_date TEXT,
       city TEXT
   );
   ```

4. Choose **File → Import → Table from CSV file**.
5. Select `sales_data.csv`, set the table name to `sales`, and confirm that the first row contains column names.
6. Open `queries.sql`, copy the queries into the **Execute SQL** tab, and run them one at a time.
7. View the results in the query results panel.

### Option 2: SQLite command line
Create the database and table using the SQL above, then import the CSV:

```text
.mode csv
.import --skip 1 sales_data.csv sales
```

Run queries from the terminal with:

```text
.read queries.sql
```

If your SQLite version does not support `--skip 1`, use the DB Browser import method instead.

## SQL Concepts Demonstrated
| SQL concept | Purpose |
|---|---|
| `SELECT` | Retrieve data from a table |
| `WHERE` | Filter rows based on a condition |
| `ORDER BY` | Sort query results |
| `GROUP BY` | Group rows with matching values |
| `COUNT()` | Count rows |
| `SUM()` | Calculate a total |
| `AVG()` | Calculate an average |
| `HAVING` | Filter grouped results |

## Business Questions Answered
1. How many sales records are in the dataset?
2. What is the total quantity sold?
3. What is the average product price?
4. What is the total sales revenue?
5. Which product categories have the most sales records?
6. Which category generates the highest revenue?
7. Which city generates the highest revenue?
8. Which products have the highest total quantity sold?

## Revenue Calculation
Revenue for each row is calculated as:

`quantity * price`

Total revenue is calculated using:

```sql
SELECT SUM(quantity * price) AS total_revenue
FROM sales;
```

## Project Outcome
After running the queries, you will have practiced core SQL operations and produced summaries of sales, revenue, products, categories, and cities.

## Future Improvements
- Add more records or use a real-world public sales dataset.
- Analyze monthly sales trends.
- Create views for frequently used summaries.
- Connect the database to Python or a visualization tool such as Power BI.

## Author
Add your name here.

## License
This project is available for educational and learning purposes.
