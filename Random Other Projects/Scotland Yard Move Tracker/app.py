from flask import Flask, render_template, request, session
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
                            move_list.remove(space)
                else:
                    print("No moves")
            case "5":
                if len(move_list) <= 0:
                    move_list.append([])
                spaces = [int(num) for num in input("What spaces to add? ").split(" ")]
                for space in spaces:
                    if space not in move_list[-1]:
                        move_list.append(space)
            case "6":
                if len(move_list) > 1:
                    move_list.pop(-1)
                print(move_list[-1])
            case "7":
                break
        print()

app = Flask(__name__)
app.secret_key = "s3cr3tk3y"

# move_list = []

@app.route("/", methods=["GET", "POST"])
def home():
    move_list = session.get("move_list", [])
    input_text = ""
    updated_text = ""
    previous_header = "-1"

    if request.method == "POST":
        input_text = request.form.get("text_field", "")
        button = request.form.get("button")
        if input_text != "":

            move_list.append(sorted(list(set([val for val in input_text.split()] if input_text != "" else []))))
            endings = []

            # Handle each button
            if button == "Taxi":
                previous_header = "  ".join(move_list[-1])
                for start in move_list[-1]:
                    try:
                        if int(start) in taxis:
                            endings.extend(taxis[int(start)])
                    except:
                        return render_template("index.html", text="", previous="", current="")
                endings = sorted(list(set(endings)))
                updated_text = "  ".join([str(val) for val in endings])
            elif button == "Bus":
                previous_header = "  ".join(move_list[-1])
                for start in move_list[-1]:
                    try:
                        if int(start) in buses:
                            endings.extend(buses[int(start)])
                    except:
                        return render_template("index.html", text="", previous="-1", current="")
                endings = sorted(list(set(endings)))
                updated_text = "  ".join([str(val) for val in endings])
            elif button == "Metro":
                previous_header = "  ".join(move_list[-1])
                for start in move_list[-1]:
                    try:
                        if int(start) in metros:
                            endings.extend(metros[int(start)])
                    except:
                        return render_template("index.html", text="", previous="-1", current="")
                endings = sorted(list(set(endings)))
                updated_text = "  ".join([str(val) for val in endings])
            elif button == "Mystery":
                previous_header = "  ".join(move_list[-1])
                for start in move_list[-1]:
                    for moves in [taxis, buses, metros, ferries]:
                        try:
                            if int(start) in moves:
                                endings.extend(moves[int(start)])
                        except:
                            return render_template("index.html", text="", previous="-1", current="")
                endings = sorted(list(set(endings)))
                updated_text = "  ".join([str(val) for val in endings])
            elif button == "Revealed":
                previous_header = "-1"
                updated_text = ""
                move_list = []
            elif button == "Rewind":
                if len(move_list) > 0:
                    move_list.pop(-1)
                    updated_text = "  ".join(move_list[-1]) if len(move_list) > 0 else ""
                    if len(move_list) > 0:
                        move_list.pop(-1)
                    previous_header = "  ".join(move_list[-1]) if len(move_list) > 0 else "-1"
                else:
                    updated_text = ""
                    previous_header = "-1"

        if previous_header == "-1" and len(move_list) > 0:
            previous_header = "  ".join(move_list[-1])

    session["move_list"] = move_list
    return render_template("index.html", text=updated_text, previous=previous_header, current=updated_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    # cli()
