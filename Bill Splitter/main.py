class list_guests():
    def __init__(self, number):
        self.guests = {}
        self.number = number

        self.exception_list()

    def name_guest(self):
        print("Enter the name of every friend (including you), each on a new line: ")
        for i in range(self.number):
            name = input()
            self.guests[name] = 0
        # print(self.guests)
        return self.guests

    def cost(self, bill):

        bill_each = round(bill / self.number, 2)
        for name in self.guests:
            up_dick = {name: bill_each}
            self.guests.update(up_dick)
        # print(self.guests)
        return self.guests

    def lucky(self, bill):
        import random
        answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: \n')

        if answer.lower() == "yes":
            random_name = random.choice(list(self.guests))
            print(f"{random_name} is the lucky one!")

            bill_each = round(bill / (self.number - 1), 2)
            for name in self.guests:
                up_dick = {name: bill_each}
                self.guests.update(up_dick)
            # print(self.guests)
            up_dick_random = {random_name: 0}
            self.guests.update(up_dick_random)
        else:
            print("No one is going to be lucky")
        return self.guests

    def exception_list(self):
        try:
            message = "No one is joining for the party"
            assert self.number > 0, message
            self.name_guest()
            bill = float(input("Enter the total bill value: \n"))
            self.cost(bill)
            self.lucky(bill)
            print(self.guests)
        except AssertionError:
            print('No one is joining for the party')


list_guests(int(input("Enter the number of friends joining (including you): \n")))