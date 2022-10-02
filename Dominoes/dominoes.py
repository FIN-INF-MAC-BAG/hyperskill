import random


class Dominos:
    def __init__(self):
        print(70 * '=')
        self.domino_set = []

        self.play()

    def create_setup(self):

        for i in range(1, 7):
            for j in range(i, 7):
                self.domino_set.append([i, j])
        random.shuffle(self.domino_set)
        return self.domino_set

    def print_status(self, stock, domino, computer_pieces, player_pieces):
        print(70 * '=')
        print('Stock size:', len(stock))
        print('Computer pieces:', len(computer_pieces), '\n')
        print(domino, '\n')
        print('Your pieces:')
        l = 1
        for i in player_pieces:
            print(f'{l}: {i}')
            l += 1

    def play_continue(self, n, lista, domino_snake, stock_pieces):
        if n > 0:
            n -= 1
            wstawka = lista[n]
            lista.pop(n)
            domino_snake.append(wstawka)
        elif n < 0:
            n *= -1
            n -= 1
            wstawka = lista[n]
            lista.pop(n)
            domino_snake.insert(0, wstawka)
        elif n == 0:
            n = random.randint(-len(lista), len(lista))
            n *= 1
            n -= 1
            wstawka = stock_pieces[n]
            stock_pieces.pop(n)
            lista.append(wstawka)
        return lista, domino_snake, stock_pieces

    def play_end_comp(self, computer_pieces, player_pieces, domino, stock_pieces):
        while computer_pieces != [] or not player_pieces != []:
            print(input("\nStatus: Computer is about to make a move. Press Enter to continue...\n"))
            n = random.randint(-len(computer_pieces), len(computer_pieces))
            computer_pieces, domino, stock_pieces = self.play_continue(n, computer_pieces, domino, stock_pieces)
            self.print_status(stock_pieces, domino, computer_pieces, player_pieces)
            print("\nStatus: It's your turn to make a move. Enter your command.")

            while True:
                try:
                    n = int(input())
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue

            player_pieces, domino, stock_pieces = self.play_continue(n, player_pieces, domino, stock_pieces)
            self.print_status(stock_pieces, domino, computer_pieces, player_pieces)
        if not computer_pieces:
            print("Status: The game is over. The computer won!")
        elif not player_pieces:
            print("Status: The game is over. You won!")
        else:
            print("Status: The game is over. It's a draw!")

    def play(self):
        self.domino_set = self.create_setup()
        comp = []
        play = []

        stock_pieces = random.sample(self.domino_set, 14)
        computer_pieces = random.sample(self.domino_set, 7)
        player_pieces = random.sample(self.domino_set, 7)
        print('Stock size:', len(stock_pieces))
        # print(computer_pieces)
        # print(player_pieces)
        for i in computer_pieces:
            if i[0] == i[1]:
                comp.append(i)

        for i in player_pieces:
            if i[0] == i[1]:
                play.append(i)

        if sum(max(comp)) > sum(max(play)):
            domino = []
            domino_snake = max(comp)
            domino.append(domino_snake)
            position = computer_pieces.index(max(comp))
            computer_pieces = computer_pieces[:position] + computer_pieces[position + 1:]
            print('Computer pieces:', len(computer_pieces), '\n')
            print(domino, '\n')
            print('Your pieces:')
            l = 1
            for i in player_pieces:
                print(f'{l}: {i}')
                l += 1

            print("\nStatus: It's your turn to make a move. Enter your command.")

            while True:
                try:
                    n = int(input())
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
            player_pieces, domino, stock_pieces = self.play_continue(n, player_pieces, domino, stock_pieces)
            self.print_status(stock_pieces, domino, computer_pieces, player_pieces)
            self.play_end_comp(computer_pieces, player_pieces, domino, stock_pieces)



        else:
            domino = []
            domino_snake = max(play)
            domino.append(domino_snake)
            position = player_pieces.index(max(play))
            player_pieces = player_pieces[:position] + player_pieces[position + 1:]
            print('Computer pieces:', len(computer_pieces), '\n')
            print(max(play), '\n')
            print('Your pieces:')
            l = 1
            for i in player_pieces:
                print(f'{l}: {i}')
                l += 1
            print(input("\nStatus: Computer is about to make a move. Press Enter to continue...\n"))
            n = random.randint(-len(computer_pieces), len(computer_pieces))
            computer_pieces, domino, stock_pieces = self.play_continue(n, computer_pieces, domino, stock_pieces)
            self.print_status(stock_pieces, domino, computer_pieces, player_pieces)
            self.play_end_comp(computer_pieces, computer_pieces, domino, stock_pieces)


Dominos()