# Connection-test


Here’s a professional **README.md** for your project:

---

# Marlyn Equipment Management System  
**Python + MySQL Integration for Infrastructure Monitoring**  

![Python](https://img.shields.io/badge/Python-3.9-blue)  
![MySQL](https://img.shields.io/badge/MySQL-8.0-green)  
![Docker](https://img.shields.io/badge/Docker-✅-blue)  

---

## **Overview**  
This project provides a Python-based interface to interact with a MySQL database (`marlyn_db`) for managing infrastructure equipment (e.g., fiber cables, routers, splice trays). It includes:  
- **Database Schema**: `COMMON_EQUIPMENT_LAN` table for tracking equipment status, location, and maintenance needs.  
- **Docker Integration**: Pre-configured MySQL and Python environments for GitHub Codespaces.  
- **Sample Queries**: Scripts for inserting, updating, and retrieving equipment data.  

---

## **Features**  
✅ Track equipment status (Active/Inactive/Maintenance).  
✅ Prioritize maintenance tasks with `maintenance = 1` flags.  
✅ Bulk insert data via CSV files.  
✅ Dockerized setup for isolated development.  

---

## **Setup Instructions**  

### **1. Prerequisites**  
- **GitHub Codespace**: Create a new codespace for this repository.  
- **Docker**: Ensure Docker is enabled in your codespace.  

### **2. Start the Environment**  
```bash  
# Build and start containers  
docker-compose up --build  
```  

### **3. Access the Database**  
Connect to MySQL via CLI:  
```bash  
docker exec -it mysql mysql -u marlyn_user -p  
# Password: marlyn_pass  
```  

---

## **Database Schema**  
**Table**: `COMMON_EQUIPMENT_LAN`  

| Column             | Type         | Description                              |  
|---------------------|--------------|------------------------------------------|  
| `eq_id`            | VARCHAR(255) | Unique equipment ID (Primary Key)        |  
| `eq_type`          | VARCHAR(255) | Equipment type (e.g., "Fiber Cable")     |  
| `status`           | VARCHAR(50)  | Current status (Active/Inactive/Maintenance) |  
| `location`         | VARCHAR(255) | Physical location (e.g., "Building A")   |  
| `maintenance`      | TINYINT      | `1` = Needs repair, `0` = Operational    |  
| `installation_date`| DATE         | Date of installation                     |  
| `manufacturer`     | VARCHAR(100) | Equipment manufacturer                   |  
| `serial_number`    | VARCHAR(50)  | Serial number                            |  

---

## **Usage**  

### **Insert Sample Data**  
```python  
python insert_data.py  
```  

### **Query Maintenance Equipment**  
```python  
python query_maintenance.py  
```  

### **Bulk Import from CSV**  
```bash  
# Place your CSV in the project root and run:  
python import_csv.py --file equipment.csv  
```  

---

## **Example Queries**  

#### **List All Equipment**  
```sql  
SELECT * FROM COMMON_EQUIPMENT_LAN;  
```  

#### **Find Equipment Needing Maintenance**  
```sql  
SELECT eq_id, eq_type, location  
FROM COMMON_EQUIPMENT_LAN  
WHERE maintenance = 1;  
```  

---

## **Troubleshooting**  
- **Connection Errors**:  
  - Verify `docker-compose.yml` credentials match your script’s config.  
  - Ensure the MySQL container is running (`docker ps`).  
- **Data Not Inserting**:  
  - Check for duplicate `eq_id` values (primary key constraint).  

---

## Contributing
1. Fork the repository.  
2. Create a feature branch (`git checkout -b feature/new-query`).  
3. Commit changes (`git commit -m "Add new query"`).  
4. Push and open a pull request.  
