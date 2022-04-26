from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def root():
    return jsonify("ok /")

@app.route('/api/health',methods=['GET'])
def health():
    return jsonify("ok /api/health")

@app.route('/hello',methods=['GET'])
def hello():
    return jsonify({'mensaje' : 'Hello world'})

@app.route('/headers',methods=['GET'])
def headers():
    return dict(request.headers)

if __name__ == '__main__':
    app.run()
