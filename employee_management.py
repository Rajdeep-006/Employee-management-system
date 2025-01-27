import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('employee_management.db')
cursor = conn.cursor()

# Create table for employee records
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employee(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Position TEXT NOT NULL,
    Salary REAL NOT NULL
)
''')

# Function to display all employee records
def list_employees():
    cursor.execute('SELECT * FROM Employee')
    employees = cursor.fetchall()
    if employees:
        for emp in employees:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Position: {emp[2]}, Salary: {emp[3]}")
    else:
        print("No employee records found.")

# Function to add a new employee
def add_employee(name, position, salary):
    cursor.execute('INSERT INTO Employee (Name, Position, Salary) VALUES (?, ?, ?)', (name, position, salary))
    conn.commit()
    print("Employee added successfully.")

# Function to update an employee's details
def update_employee(emp_id, new_name, new_position, new_salary):
    cursor.execute('UPDATE Employee SET Name=?, Position=?, Salary=? WHERE ID=?', (new_name, new_position, new_salary, emp_id))
    conn.commit()
    print("Employee details updated successfully.")

# Function to delete an employee record
def delete_employee(emp_id):
    cursor.execute('DELETE FROM Employee WHERE ID=?', (emp_id,))
    conn.commit()
    print("Employee record deleted successfully.")

# Main menu
def main():
    while True:
        print("\nEmployee Management System")
        print("1. List all employees")
        print("2. Add a new employee")
        print("3. Update an employee's details")
        print("4. Delete an employee")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_employees()
        elif choice == '2':
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = float(input("Enter employee salary: "))
            add_employee(name, position, salary)
        elif choice == '3':
            emp_id = int(input("Enter employee ID to update: "))
            new_name = input("Enter new name: ")
            new_position = input("Enter new position: ")
            new_salary = float(input("Enter new salary: "))
            update_employee(emp_id, new_name, new_position, new_salary)
        elif choice == '4':
            emp_id = int(input("Enter employee ID to delete: "))
            delete_employee(emp_id)
        elif choice == '5':
            print("Exiting Employee Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
