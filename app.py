from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            operation = request.form["operation"]

            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            else:
                error = "Invalid operation"

        except (ValueError, KeyError):
            error = "Enter valid numbers and select an operation"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kubernetes Calculator</title>
    </head>
    <body>
        <h1>Menu-Driven Calculator</h1>
        <form method="post">
            <label>First number:</label>
            <input type="number" step="any" name="a" required>
            <br><br>
            <label>Second number:</label>
            <input type="number" step="any" name="b" required>
            <br><br>
            <button name="operation" value="add">Addition</button>
            <button name="operation" value="subtract">Subtraction</button>
        </form>
        <h2>Result: {result if result is not None else ""}</h2>
        <p>{error or ""}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)