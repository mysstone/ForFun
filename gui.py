import sqlite3
import time


conn = sqlite3.connect("cust.db")
cur = conn.cursor()


anson = True


while anson:
    print("Welcome to customer database! Please select options: \n|A| Search for username"
          "\n|B| Create new user"
          "\n|C| Update user info\nType 'q' to exit.")

    answer = input("")
    if answer == "q":
        conn.commit()
        conn.close()
        print("Goodbye!")
        break

    if answer == "a" or answer == "A":
        print("You selected A")
        search = True
        while search:
            question = str(input("Search for query. Press 's' to stop and go to main menu:\n"))
            if question == "s":
                break
            question = question.strip()

            query = "SELECT * FROM customers WHERE first_name = ?"

            cur.execute(query, (question, ))

            result = cur.fetchone()

            print(result)

    elif answer == "b" or answer == "B":
        print("You selected B")
        search = True
        while search:
            first_name = str(input("Create new user. Type your first name: Press 's' to stop and go to main menu:\n"))
            if first_name == "s":
                break
            first_name = first_name.strip()
            last_name = str(input("Now please type your last name:"))
            if last_name == "":
                print("Must enter a value")
            continue
        query = "INSERT INTO customers(first_name, last_name, age, address) values (?, ?, ?,?)"

    elif answer == "c" or answer == "C":
        print("You selected C")

        last_lookup = str(input("Please type your last name to search. Type 's' to stop and go to main menu:\n"))
        last_lookup = last_lookup.strip()
        last_lookup = last_lookup.capitalize()

        if last_lookup == "s":
            break

        query = "SELECT * FROM customers where last_name=?"

        result = cur.execute(query, (last_lookup,))
        row = result.fetchone()
        if row is None:
            print("No user found. Please try again")
        else:
            print(f'------------------------------------------------------------------------------\n'
                  f'ID {row[0]} was found in the database. here is the information:\n'
                  f'First name: {row[1]}\nLast Name: {row[2]}\nAge: {row[3]}\nAddress: {row[4]}'
                  f'\n------------------------------------------------------------------------------')
            time.sleep(3)

    else:
        print("Oh no. No option selected. Please try again. ")
    continue




