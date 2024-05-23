from flask import Flask, request
from flask_cors import CORS
from wompi.wompi import get_cc_link
import government.government as government
import json


app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['POST'])
def api():
    # Get the JSON data from the request
    data = json.loads(list(dict(request.form).keys())[0])
    print(data)
    data = dingly_do(data)
    if data["type"] == "wompi":
        try:
            print("\n"*10)
            cc_link =  get_cc_link(data)
            print(f"Link: {cc_link}")
            return {"link": cc_link}, 200
        except Exception as e:
            print(str(e))
            return {"link": "error"}, 400
        
    elif data["type"] == "government":
        try:
            print("\n"*10)
            invoice = government.get_government_invoice(data)
            print(f"invoice: {invoice}")
            return {"invoice": invoice}, 200
        except Exception as e:
            print(str(e))
            return {"invoice": "error"}, 400
    else:
        print("Missing requirements")

        return ({'link' if data["type"] == 'wompi' else "invoice": 'error'}),404
    
# make sure required data is present and replace " " with "+"                                                                                                                                      
def dingly_do(data):
    for i in data:
        if(data["type"] == "wompi"):
            data[i] = data[i].replace(" ","+")
    return data

if __name__ == '__main__':
    app.run(debug=True)
