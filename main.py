from flask import (Flask, render_template, request, make_response)
import json
import uuid

app = Flask('app')


@app.route('/', methods=['POST', 'GET'])
def calculate():
    data = dict(request.form.items())
    val1 = int(data.get('val1', 0))
    val2 = int(data.get('val2', 0))
    total_val = val1 + val2
    id_current = str(uuid.uuid1())
    existing_data = get_data()
    existing_data[id_current] = "The sum of {} and {} is {}".format(val1,val2,total_val)
    context = {'data': existing_data}
    response = make_response(render_template("index.html", **context))
    response.set_cookie('historical_calculator', json.dumps(existing_data))
    return response


def get_data():
    data = request.cookies.get('historical_calculator')
    try:
        data_dict = json.loads(data)
    except TypeError:
        data_dict = {}
    return data_dict

app.run(debug=True, host='0.0.0.0', port=8080)
