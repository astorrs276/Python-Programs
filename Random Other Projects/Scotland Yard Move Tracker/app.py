from flask import Flask, render_template, request, session
import os
from move_lists import taxis, buses, metros, ferries

app = Flask(__name__)
app.secret_key = os.urandom(24)

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

            move_list.append(sorted(list(set(input_text.split()))))
            endings = []

            # Handle each button
            if button == "Taxi":
                previous_header = "  ".join(move_list[-1])
                for start in move_list[-1]:
                    try:
                        if int(start) in taxis:
                            endings.extend(taxis[int(start)])
                    except ValueError:
                        move_list = []
                        return render_template("index.html", text="", previous="-1", current="")
                endings = sorted(list(set(endings)))
                updated_text = "  ".join([str(val) for val in endings])
            elif button == "Bus":
                previous_header = "  ".join(move_list[-1])
                for start in move_list[-1]:
                    try:
                        if int(start) in buses:
                            endings.extend(buses[int(start)])
                    except ValueError:
                        move_list = []
                        return render_template("index.html", text="", previous="-1", current="")
                endings = sorted(list(set(endings)))
                updated_text = "  ".join([str(val) for val in endings])
            elif button == "Metro":
                previous_header = "  ".join(move_list[-1])
                for start in move_list[-1]:
                    try:
                        if int(start) in metros:
                            endings.extend(metros[int(start)])
                    except ValueError:
                        move_list = []
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
                        except ValueError:
                            move_list = []
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
    app.run(host="0.0.0.0", port=5000, debug=False)
