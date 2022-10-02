import random
import sys
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INT DEFAULT 0);')
conn.commit()


class Bank:
    def __init__(self):
        self.users = []
        self.main()

        self.cur = cur

    def number_randomly(self, x):
        number = ""
        if x == "ACCOUNT":
            for i in range(9):
                random_digit = random.randrange(0, 10)
                number = number + str(random_digit)
        else:
            number = str(random.choice(range(10000))).zfill(4)
        return number

    def last_digit(self, iin, ai):
        p = []
        c = []
        f = 1
        for i in iin:
            p.append(i)
        for k in ai:
            p.append(k)
        for h in p:
            h = (int(h) * 2 if f % 2 != 0 else int(h))
            if h > 9:
                h -= 9
                c.append(h)
            else:
                c.append(h)
            f += 1
        last = str(10 - sum(c) % 10)

        return last

    def create_account(self):
        iin = '400000'
        ai = self.number_randomly("ACCOUNT")
        pin = self.number_randomly("PIN")
        last_digit = self.last_digit(iin, ai)
        account_number = iin + ai + last_digit
        print("\nYour card has been created\nYour card number:\n", account_number,
              "\nYour card pin:\n{0}\n".format(int(pin)))
        # account = self.create_user(account_nr=account_number, account_pin=pin)
        # self.users.append(account)

        insert_query = "INSERT INTO card (number,pin) VALUES (?,?);"
        values = (account_number, pin)
        cur.execute(insert_query, values)
        conn.commit()

        # return self.users

    def create_user(self, **kwargs):
        return kwargs

    def login(self):
        given_account_number = input("Enter your card number:\n")
        given_pin = input("Enter your PIN:\n")
        cur.execute("Select number, pin, balance from card")
        for user in cur:
            if given_account_number == user[0] and given_pin == user[1]:
                print("You have successfully logged in!\n")
                while True:
                    print("1. Balance")
                    print("2. Log out")
                    print("0. Exit")
                    choice_log = int(input())
                    if choice_log == 1:
                        print(user[2])
                    elif choice_log == 2:
                        print("You have successfully logged out!")
                        break
                    else:
                        print("Bye!")
                        sys.exit()
            else:
                continue
                if given_account_number != user[0] and given_pin != user[1]:
                    print("Wrong card number or PIN!")
                    break

    def main(self):
        while True:
            print("1. Create an account")
            print("2. Log into account")
            print("0. Exit\n")
            choice = int(input())
            if choice == 1:
                self.create_account()
            elif choice == 2:
                self.login()
            else:
                print("Bye!")
                break


Bank()
