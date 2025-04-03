import mysql.connector  

# Database config  
config = {  
    'host': 'localhost',  
    'user': 'root',             # Use 'marlyn_user' if created  
    'password': 'root',  
    'database': 'marlyn_db'  
}  

equipment_data = [  
    ('Fiber Cable', 'Active', 'Building A', 1),  
    ('Router', 'Inactive', 'Floor 2', 0),  
    ('Splice Tray', 'Maintenance', 'Rack 5', 1),  
    ('Patch Panel', 'Active', 'Data Center', 0)  
]  
# Connect to MySQL  
try:  
    conn = mysql.connector.connect(**config)  
    cursor = conn.cursor()  
    print("Connected to MySQL!")  

    # Create a sample table  
    cursor.execute("""  
    CREATE TABLE IF NOT EXISTS equipment (  
        id INT AUTO_INCREMENT PRIMARY KEY,  
        name VARCHAR(255),  
        status VARCHAR(50)  
    )  
    """)  
    print("Table created.")  

    # Insert test data  
    cursor.execute("INSERT INTO equipment (name, status) VALUES ('Fiber Cable', 'Active')")  
    conn.commit()  
    print("Data inserted.")  

    # Fetch data  
    cursor.execute("SELECT * FROM equipment")  
    rows = cursor.fetchall()  
    print("\nEquipment List:")  
    for row in rows:  
        print(row)  

    # Insert multiple rows using parameterized query  
    insert_query = """  
    INSERT INTO COMMON_EQUIPMENT_LAN  
    (eq_type, status, location, maintenance)  
    VALUES (%s, %s, %s, %s)  
    """  
    cursor.executemany(insert_query, equipment_data)  
    conn.commit()  
    print(f"{cursor.rowcount} records inserted.")  


except mysql.connector.Error as err:  
    print(f"Error: {err}")  

finally:  
    if conn.is_connected():  
        cursor.close()  
        conn.close()  




