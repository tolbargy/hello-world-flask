from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello',methods=['GET'])
def hello():
    return jsonify({'mensaje' : 'Hello PPP'})

if __name__ == '__main__':
    app.run()