import argparse
import json
import os
import random

from collections import defaultdict
from enum import Enum
from io import StringIO
from typing import Callable, Union
from typing import Dict, Tuple, Sequence


class FlashcardMenu(Enum):
    ADD = "add"
    REMOVE = "remove"
    IMPORT = "import"
    EXPORT = "export"
    ASK = "ask"
    EXIT = "exit"
    LOG = "log"
    HARDEST_CARD = "hardest card"
    RESET_STATS = "reset stats"


class Flashcards:
    cards = dict()
    mistakes_counter = dict()
    mistakes_counter = defaultdict(int)

    def __init__(self):
        parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Flashcards")
        parser.add_argument("--import_from", help="imports card set")
        parser.add_argument("--export_to", help="exports card set")

        self.args: argparse.Namespace = parser.parse_args()

        if self.args.import_from:
            self.import_card(self.args.import_from)

        self.stringio = StringIO()
        self.menu()

    def menu(self):
        menu_actions: dict[FlashcardMenu, Callable[[], None]] = {
            FlashcardMenu.ADD: self.add,
            FlashcardMenu.REMOVE: self.remove,
            FlashcardMenu.IMPORT: self.import_prompt,
            FlashcardMenu.EXPORT: self.export_prompt,
            FlashcardMenu.ASK: self.ask,
            FlashcardMenu.EXIT: self.exit,
            FlashcardMenu.LOG: self.log,
            FlashcardMenu.HARDEST_CARD: self.hardest_card,
            FlashcardMenu.RESET_STATS: self.reset_stats,
        }

        action: Union[FlashcardMenu, None] = None
        while action != self.exit:
            print("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
            action: FlashcardMenu = FlashcardMenu(self.input_stringio())
            menu_actions[action]()

    def add(self):
        print("The card:")
        term: str = self.input_stringio()
        while term in self.cards:
            print(f'The card "{term}" already exists.')
            term = self.input_stringio()

        print("The definition of the card:")
        definition: str = self.input_stringio()
        while definition in self.cards.values():
            print(f'The card "{definition}" already exists.')
            definition = self.input_stringio()

        self.cards[term] = definition
        print(f'The pair ("{term}":"{definition}" has been added.)')

    def remove(self):
        print("Which card?")
        term: str = self.input_stringio()
        if term not in self.cards:
            print(f"""Can't remove "{term}": there is no such card.""")
        else:
            del self.cards[term]
            print("The card has been removed.")

    def import_prompt(self):
        return self.import_card(self.input_filename())

    def import_card(self, filename: str):
        if not os.access(filename, os.F_OK):
            return print("File not found.")

        with open(filename, 'r') as f:
            self.cards.update(json.load(f)[0])
        print(f"{len(self.cards)} cards have been loaded.")

    def export_prompt(self):
        return self.export(self.input_filename())

    def export(self, filename: str):
        with open(filename, 'w') as f:
            json.dump([self.cards, self.mistakes_counter], f)
        print(f"{len(self.cards)} cards have been saved.")

    def ask(self):
        print("How many times to ask?")
        ask_count: int = int(self.input_stringio())

        for i in range(ask_count):
            term: str = random.choice(list(self.cards))

            print(f'Print the definition of "{term}":')
            definition: str = self.input_stringio()
            if definition == self.cards[term]:
                print("Correct!")
                continue

            if definition in self.cards.values():
                term_of_definition: str = [k for k, v in self.cards.items() if v == definition][0]
                print(f'Wrong. The right answer is "{self.cards[term]}",'
                      f' but your definition is correct for "{term_of_definition}".')
            else:
                print(f'Wrong. The right answer is "{self.cards[term]}".')
            self.mistakes_counter[term] += 1

    def exit(self):
        print("Bye bye!")
        if self.args.export_to:
            self.export(self.args.export_to)
        exit()

    def log(self):
        filename: str = self.input_filename()
        self.stringio.seek(0)
        with open(filename, 'w') as f:
            for input_line in self.stringio.readlines():
                f.write(input_line)
        print("The log has been saved.")

    def hardest_card(self):
        max_mistake_count: int = max(self.mistakes_counter.values(), default=0)
        if max_mistake_count == 0:
            return print("There are no cards with errors.")

        max_mistake_terms: list[str] = [k for k, v in self.mistakes_counter.items() if v == max_mistake_count]
        if len(max_mistake_terms) > 1:
            terms: str = ", ".join(f'"{term}"' for term in max_mistake_terms)
            print(f"The hardest cards are, {terms}. You have {max_mistake_count} errors answering them.")
        else:
            print(f'The hardest card is "{max_mistake_terms[0]}". You have {max_mistake_count} errors answering it.')

    def reset_stats(self):
        self.mistakes_counter = defaultdict(int)
        print("Card statistics have been reset.\n")

    def input_filename(self) -> str:
        print("File name:")
        return self.input_stringio()

    def input_stringio(self) -> str:
        user_input: str = input()
        self.stringio.write(user_input + "\n")
        return user_input


def main():
    Flashcards()


if __name__ == "__main__":
    main()
