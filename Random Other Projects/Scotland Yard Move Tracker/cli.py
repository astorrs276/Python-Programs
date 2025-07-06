from move_lists import taxis, buses, metros, ferries

def test():
    checking = taxis
    missing = []
    for key in checking:
        for value in checking[key]:
            if value not in checking:
                print(value)
            elif key not in checking[value]:
                missing.append((key, value))
    print(missing)

def print_options():
    print('''1. Display possible spaces.
2. Mister X moves.
3. Mister X location revealed.
4. Remove possible spaces.
5. Add possible spaces.
6. Revert to previous
7. Exit''')

def cli():
    move_list = []
    while True:
        print_options()
        match input(">>> "):
            case "1":
                if len(move_list) > 0:
                    print(move_list[-1])
                else:
                    print("No moves")
            case "2":
                type = input("How does Mister X move (T/B/M/W)? ").upper()
                endings = []
                if type == "W":
                    for start in move_list[-1]:
                        for moves in [taxis, buses, metros, ferries]:
                            if start in moves:
                                endings.extend(moves[start])
                else:
                    moves = taxis if type == "T" else buses if type == "B" else metros
                    for start in move_list[-1]:
                        if start in moves:
                            endings.extend(moves[start])
                move_list.append(sorted(list(set(endings[:]))))
                print(move_list[-1])
            case "3":
                move_list = []
                move_list.append([int(input("Where is Mister X? "))])
                print(move_list[-1])
            case "4":
                if len(move_list) > 0:
                    spaces = [int(num) for num in input("What spaces to remove? ").split(" ")]
                    for space in spaces:
                        if space in move_list[-1]:
                            move_list[-1].remove(space)
                else:
                    print("No moves")
            case "5":
                if len(move_list) <= 0:
                    move_list.append([])
                spaces = [int(num) for num in input("What spaces to add? ").split(" ")]
                for space in spaces:
                    if space not in move_list[-1]:
                        move_list[-1].append(space)
            case "6":
                if len(move_list) > 1:
                    move_list.pop(-1)
                print(move_list[-1])
            case "7":
                break
        print()

def main():
    cli()

if __name__ == "__main__":
    main()
