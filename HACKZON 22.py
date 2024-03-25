import mysql.connector.pooling as mpool
from tabulate import tabulate


db_config = {
    "host": "localhost",
    "user": "root",
    "password": "jay",
    "database": "employees"
}


connection_pool = mpool.MySQLConnectionPool(pool_name="my_pool", pool_size=5, **db_config)

def get_connection():
    
    return connection_pool.get_connection()

def menu():
    while True:
        print("---- Welcome to the database ---")
        print("1. Access database as patient")
        print("2. Access database as staff")
        try:
            choice = int(input("Enter your choice: "))
            if choice not in [1, 2]:
                raise ValueError("Invalid choice. Please enter 1 or 2.")
            if choice == 1:
                patient()
            elif choice == 2:
                admin_menu()
        except ValueError as ve:
            print(ve)

def admin_menu():
    print("#### Admin Entry ####")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if username == "admin" and password == "adminpass":
        hospital_menu()
    else:
        print("Incorrect username or password.")
        menu()

def hospital_menu():
    print("1. Do you want to access the staff section?")
    print("2. Enter as intern")
    try:
        choice = int(input("Enter your choice: "))
        if choice not in [1, 2]:
            raise ValueError("Invalid choice. Please enter 1 or 2.")
        if choice == 1:
            doctor_menu()
        elif choice == 2:
            intern()
    except ValueError as ve:
        print(ve)
        hospital_menu()

def doctor_menu():
    while True:
        print("1. Do you want to access the HR module?")
        print("2. Do you want to access the doctor's portal?")
        try:
            choice = int(input("Enter your choice: "))
            if choice not in [1, 2]:
                raise ValueError("Invalid choice. Please enter 1 or 2.")
            if choice == 1:
                hr_module()
            elif choice == 2:
                pdoctor()
        except ValueError as ve:
            print(ve)

def pdoctor():
    while True:
        print("--- WELCOME TO DOCTORS PORTAL ---")
        print("What would you like to do?")
        print("1. View details")
        print("2. Update details")
        print("3. Delete records")
        print("4. Display details")
        print("5. Back to main menu")
        try:
            choice = int(input("Enter your choice: "))
            if choice not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid choice. Please enter a number between 1 and 5.")
            if choice == 1:
                view()
            elif choice == 2:
                update()
            elif choice == 3:
                delete()
            elif choice == 4:
                display()
            elif choice == 5:
                menu()
        except ValueError as ve:
            print(ve)

def view():
    try:
        con = get_connection()
        cursor = con.cursor()
        NO = int(input("Enter the employee number: "))
        q = "select * from DOCTOR where NO={}".format(NO)
        cursor.execute(q)
        rows = cursor.fetchall()
        if not rows:
            print("No record found.")
        else:
            print(tabulate(rows, headers=['No', 'NAME', 'DEPARTMENT', 'DATEOFJOIN', 'SALARY', 'SEX', 'AGE', 'ADDRESS', 'LEAVEBAL'], tablefmt='fancy_grid'))
    except Exception as e:
        print(e)
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

def update():
    try:
        con = get_connection()
        cursor = con.cursor()

        while True:
            EMPNO = int(input("Enter the employee number (0 to exit): "))
            if EMPNO == 0:
                break

         
            NAME = input("Enter the new name: ")
            DEPARTMENT = input("Enter the new department: ")
           

            
            params = [(NAME, DEPARTMENT, ...)]  

           
            sql = "UPDATE employees SET NAME = %s, DEPARTMENT = %s, ... WHERE EMPNO = %s"
            cursor.executemany(sql, params)

        con.commit()
        print("The records have been updated.")
    except Exception as e:
        print(e)
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

def delete():
    try:
        con = get_connection()
        cursor = con.cursor()

        while True:
            EMPNO = int(input("Enter the employee number to delete (0 to exit): "))
            if EMPNO == 0:
                break

            
            params = [(EMPNO,)]

            
            sql = "DELETE FROM employees WHERE EMPNO = %s"
            cursor.executemany(sql, params)

        con.commit()
        print("The records have been deleted.")
    except Exception as e:
        print(e)
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

def display():
    try:
        con = get_connection()
        cursor = con.cursor()
        sql = "select * from employees"
        cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            print("No records found.")
        else:
            print(tabulate(data, headers=['No', 'NAME', 'DEPARTMENT', 'DATEOFJOIN', 'SALARY', 'SEX', 'AGE', 'ADDRESS', 'LEAVEBAL'], tablefmt='fancy_grid'))
    except Exception as e:
        print(e)
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

def patient():
    while True:
        print("1. Do you want to book an appointment?")
        print("2. Buy emergency medicines")
        print("3. Book an ambulance")
        try:
            choice = int(input("Enter your option: "))
            if choice not in [1, 2, 3]:
                raise ValueError("Invalid choice. Please enter a number between 1 and 3.")
            if choice == 1:
                appointment()
            elif choice == 2:
                medicines()
            elif choice == 3:
                ambulance()
        except ValueError as ve:
            print(ve)

def appointment():
    try:
        con = get_connection()
        cursor = con.cursor()

        while True:
            
            NO = int(input("Enter the phone number (0 to exit): "))
            if NO == 0:
                break
            NAME = input("Enter the name: ")
            SEX = input("Enter the sex: ")
            AGE = int(input("Enter the age: "))
            ADDRESS = input("Enter the address: ")

            
            sql = "INSERT INTO patient (NO, NAME, SEX, AGE, ADDRESS) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (NO, NAME, SEX, AGE, ADDRESS))

        con.commit()
        print("Your appointment has been booked.")
    except Exception as e:
        print(e)
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

def medicines():
    try:
        con = get_connection()
        cursor = con.cursor()

       
        name = input("Enter the medicines you want to purchase: ")
        nos = int(input("Enter the number of units you would like to order: "))
        total = nos * name
        print("The total amount is:", total)
        print("Thank you for the purchase. You will receive your order shortly.")

        

    except Exception as e:
        print(e)
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

def ambulance():
    try:
        con = get_connection()
        cursor = con.cursor()

        inp = input("Press 1 for emergency ambulance service: ")
        if inp == '1':
            print("The ambulance is on its way.")
            print("Kindly ensure the patient has been given first aid.")

        

    except Exception as e:
        print(e)
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

menu()
