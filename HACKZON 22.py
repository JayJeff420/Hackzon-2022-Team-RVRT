import mysql.connector.pooling as mpool
from tabulate import tabulate
import bcrypt

# =========================
# DATABASE CONFIGURATION
# =========================

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "jay",
    "database": "employees"
}

POOL = mpool.MySQLConnectionPool(
    pool_name="hospital_pool",
    pool_size=5,
    **DB_CONFIG
)


class DatabaseManager:
    @staticmethod
    def get_connection():
        return POOL.get_connection()


# =========================
# AUTHENTICATION
# =========================

class AuthService:
    ADMIN_USERNAME = "admin"
    ADMIN_HASHED_PASSWORD = bcrypt.hashpw(
        b"adminpass", bcrypt.gensalt()
    )

    @staticmethod
    def authenticate(username, password):
        if username != AuthService.ADMIN_USERNAME:
            return False
        return bcrypt.checkpw(password.encode(), AuthService.ADMIN_HASHED_PASSWORD)


# =========================
# DOCTOR / EMPLOYEE SERVICE
# =========================

class EmployeeService:

    @staticmethod
    def view_employee(emp_no):
        with DatabaseManager.get_connection() as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM employees WHERE EMPNO = %s", (emp_no,))
            rows = cur.fetchall()

            if rows:
                print(tabulate(
                    rows,
                    headers=[
                        'EMPNO', 'NAME', 'DEPARTMENT', 'DATEOFJOIN',
                        'SALARY', 'SEX', 'AGE', 'ADDRESS', 'LEAVEBAL'
                    ],
                    tablefmt='fancy_grid'
                ))
            else:
                print("No record found.")

    @staticmethod
    def display_all():
        with DatabaseManager.get_connection() as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM employees")
            rows = cur.fetchall()

            if rows:
                print(tabulate(
                    rows,
                    headers=[
                        'EMPNO', 'NAME', 'DEPARTMENT', 'DATEOFJOIN',
                        'SALARY', 'SEX', 'AGE', 'ADDRESS', 'LEAVEBAL'
                    ],
                    tablefmt='fancy_grid'
                ))
            else:
                print("No records available.")

    @staticmethod
    def update_employee(emp_no, name, department):
        with DatabaseManager.get_connection() as con:
            cur = con.cursor()
            cur.execute(
                "UPDATE employees SET NAME=%s, DEPARTMENT=%s WHERE EMPNO=%s",
                (name, department, emp_no)
            )
            con.commit()
            print("Employee updated successfully.")

    @staticmethod
    def delete_employee(emp_no):
        with DatabaseManager.get_connection() as con:
            cur = con.cursor()
            cur.execute("DELETE FROM employees WHERE EMPNO=%s", (emp_no,))
            con.commit()
            print("Employee deleted successfully.")


# =========================
# PATIENT SERVICES
# =========================

class PatientService:

    @staticmethod
    def book_appointment():
        with DatabaseManager.get_connection() as con:
            cur = con.cursor()
            phone = input("Phone Number: ")
            name = input("Name: ")
            sex = input("Sex: ")
            age = int(input("Age: "))
            address = input("Address: ")

            cur.execute(
                "INSERT INTO patient (NO, NAME, SEX, AGE, ADDRESS) VALUES (%s,%s,%s,%s,%s)",
                (phone, name, sex, age, address)
            )
            con.commit()
            print("Appointment booked successfully.")

    @staticmethod
    def buy_medicine():
        MEDICINE_PRICE = {
            "paracetamol": 10,
            "ibuprofen": 15,
            "antibiotic": 25
        }

        medicine = input("Medicine name: ").lower()
        qty = int(input("Quantity: "))

        if medicine not in MEDICINE_PRICE:
            print("Medicine not available.")
            return

        total = MEDICINE_PRICE[medicine] * qty
        print(f"Total amount: ₹{total}")
        print("Order confirmed.")

    @staticmethod
    def ambulance():
        print("🚑 Ambulance dispatched. Stay calm.")


# =========================
# MENU SYSTEM
# =========================

def doctor_menu():
    while True:
        print("\nDoctor Portal")
        print("1. View employee")
        print("2. Update employee")
        print("3. Delete employee")
        print("4. Display all")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            EmployeeService.view_employee(int(input("Employee No: ")))
        elif choice == "2":
            emp = int(input("Employee No: "))
            name = input("New Name: ")
            dept = input("New Department: ")
            EmployeeService.update_employee(emp, name, dept)
        elif choice == "3":
            EmployeeService.delete_employee(int(input("Employee No: ")))
        elif choice == "4":
            EmployeeService.display_all()
        elif choice == "5":
            break


def patient_menu():
    while True:
        print("\nPatient Portal")
        print("1. Book Appointment")
        print("2. Buy Medicine")
        print("3. Ambulance")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":
            PatientService.book_appointment()
        elif choice == "2":
            PatientService.buy_medicine()
        elif choice == "3":
            PatientService.ambulance()
        elif choice == "4":
            break


def main():
    while True:
        print("\nHospital Management System")
        print("1. Admin")
        print("2. Patient")
        print("3. Exit")

        choice = input("Choice: ")

        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")

            if AuthService.authenticate(u, p):
                doctor_menu()
            else:
                print("Invalid credentials.")
        elif choice == "2":
            patient_menu()
        elif choice == "3":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
