import random
import sys


class hangman:
    def __init__(self, point_win=0, point_lost=0):
        self.word = 'python', 'java', 'swift', 'javascript'
        # self.word = 'java'
        self.point_win = point_win
        self.point_lost = point_lost
        print("H A N G M A N")
        self.menu()

        self.guess = ""

    def menu(self):
        while True:
            a = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
            if a == 'play':
                self.beginning()
                break
            elif a == 'results':
                print(f'You won: {self.point_win} times.')
                print(f'You lost: {self.point_lost} times.')
                continue
            else:
                sys.exit()

    def beginning(self):

        ra = random.choice(self.word)
        print()
        guess = "{sth}".format(sth=len(ra) * '-')
        print(guess)
        self.check_letter(ra, guess)

        # z = input("Guess the word {sth}: ".format(sth=ra[:3] + ((len(ra) - 3) * '-')))
        # if z == ra:
        #     print("You survived!")
        # else:
        #     print("You lost!")

    def check_type(self, k):

        while True:
            z = input("Input a letter: ")
            if len(z) != 1 or z == '':
                print('Please, input a single letter.\n')
                print(self.guess)

                continue
                # self.check_type(k)
            elif z in k:
                print("You've already guessed this letter.\n")
                print(self.guess)

                continue
                # self.check_type(k)
            elif z != z.lower() or not z.isalpha():
                print("Please, enter a lowercase letter from the English alphabet.\n")
                print(self.guess)

                continue
                # self.check_type(k)

            else:
                z = str(z)

                break
        return z

    def check_letter(self, re, guess):
        # p = 0
        self.guess = guess
        life = 0
        k = []
        while life != 8:

            z = self.check_type(k)
            c = re.count(str(z))
            k.append(z)
            # if z in self.guess:
            #     print("No improvements.\n")
            #     print(self.guess)
            #     life += 1
            if c != 0:
                l = []
                for i in range(0, len(re)):
                    if z == re[i]:
                        l.append(i)
                    else:
                        continue
                # for i in range(c):
                #         l.append(re[i:].find(z))
                print("\n{g}".format(g=self.print_check(l, re)))
                if self.guess == re:
                    print(f'You guessed the word {self.guess}!')
                    print('You survived!')
                    self.point_win += 1
                    self.menu()


            else:

                print("That letter doesn't appear in the word.")
                life += 1
                print("\n{g}".format(g=self.guess))
        print("You lost!")
        if life == 8:
            self.point_lost += 1
            self.menu()
        else:
            # print("We'll see how well you did in the next stage")
            self.menu()

        # print("We'll see how well you did in the next stage")

    def print_check(self, l, ra):
        gu = list(self.guess)
        for i in l:
            gu[i] = ra[i]
            self.guess = ''.join(gu)
        return self.guess


hangman()