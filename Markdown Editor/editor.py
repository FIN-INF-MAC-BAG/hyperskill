import sys

worlds = []

forbidden = []
forbidden2 = ['#', '* ', '. ']
f = open("output.md", "w")


def which_print_file(worlds):
    # res = check_kratka(worlds)
    rem = check_list(worlds)
    # if bool(res):
    #     print_list(worlds)
    if bool(rem):
        print_list3_file(worlds)
    else:
        print_list2_file(worlds)

def print_list_file(worlds):
    for i in worlds:
        print(i, end='', file=f)


def print_list2_file(worlds):
    print(''.join(worlds), end='', file=f)

def print_list3_file(worlds):
    for i in worlds:

        print(i, file=f)

    # print(file=f)

def print_list(worlds):
    for i in worlds:
        print(i, end='')



def print_list3(worlds):
    for i in worlds:
        print(i)

    print()



def check_list(worlds):
    for i in worlds:
        rem = [ele for ele in forbidden2 if ele in i]
    return rem


def check_kratka(worlds):
    for i in worlds:
        res = [ele for ele in forbidden if ele in i]
    return res


def which_print(worlds):
    # res = check_kratka(worlds)
    rem = check_list(worlds)
    # if bool(res):
    #     print_list(worlds)
    if bool(rem):
        print_list3(worlds)
    else:
        print_list2(worlds)


def print_list2(worlds):
    print(''.join(worlds))


def variables(choice):
    if choice != 'new-line' and choice != 'link' and choice != 'header' and choice != "unordered-list" and choice != "ordered-list":
        n = input("Text: ")
        return n


def header(n):
    l = int(input("Level: "))

    while l not in range(1, 7):
        print("The level should be within the range of 1 to 6")
        l = int(input("Level: "))
    text = input("Text: ")
    m = str(l * '#')
    p = f"{m} {text}"
    worlds.append(p)
    which_print(worlds)
    # print("\n")


def ordered(n):
    ko = int(input("Number of rows: "))
    while ko <= 0:
        print("The number of rows should be greater than zero")
        ko = int(input("Number of rows: "))

    if choice == 'ordered-list':
        for i in range(ko):
            row = input(f"Row #{i + 1} ")
            p = f"{i + 1}. {row}"
            worlds.append(p)
    else:
        for i in range(ko):
            row = input(f"Row #{i + 1} ")
            p = f"* {row}"
            worlds.append(p)
    which_print(worlds)
    # print("\n")


def bold(n):
    p = f"**{n}**"
    worlds.append(p)
    which_print(worlds)


def italic(n):
    p = f"*{n}*"
    worlds.append(p)
    which_print(worlds)


def bolditalic(n):
    p = f"*{n}*"
    worlds.append(p)
    which_print(worlds)


def inlinecode(n):
    p = f"`{n}`"
    worlds.append(p)
    which_print(worlds)


def link(n):
    label = input("Label: ")
    url = input("URL: ")
    p = f"[{label}]({url})"
    worlds.append(p)
    which_print(worlds)


def newline(n):
    p = f"\n"
    worlds.append(p)
    which_print(worlds)


def plain(n):
    p = f"{n}"
    worlds.append(p)
    which_print(worlds)


while True:
    # variables()
    functions = {
        "header": header,
        "bold/italic": bolditalic,
        "inline-code": inlinecode,
        "link": link,
        "bold": bold,
        "italic": italic,
        "new-line": newline,
        "plain": plain,
        "ordered-list": ordered,
        "unordered-list": ordered,

    }
    # functions = ['header', 'bold', 'italic', 'bold/italic', "inline-code", "link", "new-line", "plain"]
    choice = input("Choose a formatter: ")

    if choice == "!help":
        print(
            "Available formatters: plain bold italic header link inline-code new-line\n"
            "Special commands: !help !done")
    elif choice == "!done":
        which_print_file(worlds)
        f.close()
        sys.exit()
    elif choice in functions:
        strategy = functions[choice]
        strategy(variables(choice))
    else:
        print("Unknown formatting type or command")

        continue
