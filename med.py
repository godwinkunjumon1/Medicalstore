import mysql.connector
from mysql.connector import Error

# Database connection
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="", 
            password="",
            database="medical_store"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None


def add_medicine(connection, name, brand, price, quantity):
    cursor = connection.cursor()
    query = "INSERT INTO medicines (name, brand, price, quantity) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, brand, price, quantity))
    connection.commit()
    print("Medicine added successfully.")


def view_medicines(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM medicines"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)


def update_medicine_quantity(connection, medicine_id, new_quantity):
    cursor = connection.cursor()
    query = "UPDATE medicines SET quantity = %s WHERE id = %s"
    cursor.execute(query, (new_quantity, medicine_id))
    connection.commit()
    print("Medicine quantity updated.")


def delete_medicine(connection, medicine_id):
    cursor = connection.cursor()
    query = "DELETE FROM medicines WHERE id = %s"
    cursor.execute(query, (medicine_id,))
    connection.commit()
    print("Medicine deleted.")


def add_customer(connection, name, contact, address):
    cursor = connection.cursor()
    query = "INSERT INTO customers (name, contact, address) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, contact, address))
    connection.commit()
    print("Customer added successfully.")


def record_sale(connection, medicine_id, customer_id, quantity_sold):
    cursor = connection.cursor()
    query = "INSERT INTO sales (medicine_id, customer_id, quantity_sold) VALUES (%s, %s, %s)"
    cursor.execute(query, (medicine_id, customer_id, quantity_sold))


    query_update = "UPDATE medicines SET quantity = quantity - %s WHERE id = %s"
    cursor.execute(query_update, (quantity_sold, medicine_id))
    
    connection.commit()
    print("Sale recorded and stock updated.")


def view_sales(connection):
    cursor = connection.cursor()
    query = """
    SELECT sales.id, medicines.name, customers.name, sales.quantity_sold, sales.sale_date
    FROM sales
    JOIN medicines ON sales.medicine_id = medicines.id
    JOIN customers ON sales.customer_id = customers.id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)


def main():
    connection = connect_to_db()
    if connection:
        while True:
            print("\n=== Medical Store Management System ===")
            print("1. Add Medicine")
            print("2. View Medicines")
            print("3. Update Medicine Quantity")
            print("4. Delete Medicine")
            print("5. Add Customer")
            print("6. Record Sale")
            print("7. View Sales")
            print("8. Exit")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter medicine name: ")
                brand = input("Enter brand: ")
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
                add_medicine(connection, name, brand, price, quantity)

            elif choice == "2":
                view_medicines(connection)

            elif choice == "3":
                medicine_id = int(input("Enter medicine ID: "))
                new_quantity = int(input("Enter new quantity: "))
                update_medicine_quantity(connection, medicine_id, new_quantity)

            elif choice == "4":
                medicine_id = int(input("Enter medicine ID: "))
                delete_medicine(connection, medicine_id)

            elif choice == "5":
                name = input("Enter customer name: ")
                contact = input("Enter contact: ")
                address = input("Enter address: ")
                add_customer(connection, name, contact, address)

            elif choice == "6":
                medicine_id = int(input("Enter medicine ID: "))
                customer_id = int(input("Enter customer ID: "))
                quantity_sold = int(input("Enter quantity sold: "))
                record_sale(connection, medicine_id, customer_id, quantity_sold)

            elif choice == "7":
                view_sales(connection)

            elif choice == "8":
                print("Exiting...")
                connection.close()
                break

            else:
                print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
