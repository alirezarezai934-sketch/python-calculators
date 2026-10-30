
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():

    result = None

    if request.method == "POST":

        choice = request.form["choice"]

        a = float(request.form.get("a") or 0)
        b = float(request.form.get("b") or 0)

        if choice == "1":
            result = a + b

        elif choice == "2":
            result = abs(a - b)

        elif choice == "3":
            result = pow(a, b)

        elif choice == "4":
            if b != 0:
                q, r = divmod(a, b)
                result = f"Quotient: {q} | Remainder: {r}"
            else:
                result = "Cannot divide by zero!"

        elif choice == "5":
            digits = int(request.form.get("digits") or 0)
            result = round(a, digits)

        elif choice == "6":
            result = f"Max: {max(a,b)} | Min: {min(a,b)}"

        elif choice == "7":
            c = float(request.form.get("c") or 0)
            result = sum([a, b, c])

        elif choice == "8":
            result = int(a)

        elif choice == "9":
            result = float(a)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
