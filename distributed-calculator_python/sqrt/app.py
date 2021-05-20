

# ------------------------------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------------------------------

import flask
from flask import request, jsonify
from flask_cors import CORS
import math
import sys

app = flask.Flask(__name__)
CORS(app)

@app.route('/sqrt', methods=['POST'])
def sqrt():
    content = request.json
    [operand_one] = [float(content['operandOne'])]
    print(f"Square root of {operand_one}", flush=True)
    return jsonify(math.sqrt(operand_one)

app.run()

