

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

@app.route('/add', methods=['POST'])
def add():
    content = request.json
    [operand_one, operand_two] = [float(content['operandOne']), float(content['operandTwo'])]
    print(f"Adding {operand_one} + {operand_two}", flush=True)
    return jsonify(math.ceil(operand_one + operand_two))

app.run(host='0.0.0.0', port=6000)


