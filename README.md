# ShopMate: Retail Inventory Manager

## Project Overview
ShopMate is a Command Line Interface (CLI) application designed to assist small retail store owners in managing their inventory. In a busy retail environment, manual tracking often leads to stockouts or discrepancies. I built this tool to automate the tracking process, allowing users to add products, process sales in real-time, and receive immediate alerts when stock levels run low.

## Theme
Retail & E-commerce

## Course
CSE1003 - Introduction to Problem Solving & Programming

## Key Features
* **Inventory Tracking:** Add new products with names and initial quantities.
* **Sales Processing:** Updates stock levels dynamically. It includes validation logic to prevent selling more items than are currently available.
* **Search Functionality:** Implements a linear search algorithm to find products by name within the database.
* **Low Stock Alerts:** Automatically flags items that drop below 10 units so they can be restocked.
* **Data Persistence:** Uses File I/O to save the inventory to `shop_data.txt`, ensuring no data is lost when the program closes.

## Project Architecture
To ensure the code is maintainable and follows the principles of modular design, I split the project into three distinct Python modules:

### 1. `main.py` (The Interface)
* Acts as the entry point for the application.
* Contains the main `while` loop and menu system.
* Handles user input and prints feedback (e.g., "Sale successful" or "Item not found").
* Connects the logic layer with the database layer.

### 2. `database.py` (The Storage Layer)
* Manages all file handling operations.
* `save_db(list)`: Iterates through the inventory list and writes it to a text file using a pipe (`|`) separator.
* `load_db()`: Reads the text file, splits the data strings, and converts numerical values from strings back to integers for calculation.

### 3. `inventory.py` (The Logic Layer)
* Contains the core algorithms for the shop.
* `process_sale()`: Checks availability and subtracts the sold quantity from the current stock (State Management).
* `get_stock_warning()`: A helper function that returns a warning message if stock < 10.

## How to Run the Application
1.  Ensure Python 3.x is installed on your machine.
2.  Download all three files (`main.py`, `database.py`, `inventory.py`) into the same folder.
3.  Open your terminal or command prompt in that directory.
4.  Run the following command:
    ```bash
    python main.py
    ```
5.  Follow the on-screen prompts to manage your shop.

## Data Storage Format
The inventory is stored in a plain text file (`shop_data.txt`) to keep the system lightweight.
**Format:** `ProductName|Quantity`
**Example:**
```text
Blue Pen|45
Notebook|12
Eraser|8
