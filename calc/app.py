from flask import Flask,request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/<oper>')
def operation(oper):
    return f"""
        <form method="POST">
            <h1>Simple Calculator</h1>
            <h3>Enter Numbers to Calculate:</h3>
            <input type="text" placeholder="number 1" name="num1">
            <p style="display:inline">{operations(oper)}</p>
            <input type="text" placeholder="number 2" name="num2">
            <button>Calculate</button>
        </form>
    """

@app.route("/<oper>", methods=["POST"])
def handle_oper(oper):
    opers = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div
    }
    num1 = int(request.form["num1"])
    print(type(num1))
    num2 = int(request.form["num2"])
    return f'{num1} {operations(oper)} {num2} = {opers[oper](num1,num2)}'

def operations(oper):
    opers = {
        'add': '+',
        'sub': '-',
        'mult': '*',
        'div': '/'
    }
    return opers[oper]
