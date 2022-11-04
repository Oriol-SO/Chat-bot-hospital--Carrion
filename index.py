from flask import Flask, render_template,request,jsonify
from chat import get_response
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('base.html')
@app.post('/message')
def message():
    text =request.get_json().get("message")
    response=get_response(text)
    message={"answer":response}
    return jsonify(message)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    print(req)
    return {
        'fulfillmentText': 'Hello from the bot world'
    }

if __name__=='__main__':
    app.run(debug=True)
