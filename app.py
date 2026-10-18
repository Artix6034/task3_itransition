
from flask import Flask, request, Response
from math import lcm
import re

app = Flask(__name__)

@app.get("/<email>")
def calculate(email):
    x = request.args.get("x")
    y = request.args.get("y")

    if (
        x is None or y is None
        or re.fullmatch(r"[0-9]+", x) is None
        or re.fullmatch(r"[0-9]+", y) is None
    ):
        return Response("NaN", mimetype="text/plain")

    result = lcm(int(x), int(y))
    return Response(str(result), mimetype="text/plain")
