from flask import Flask , render_template,jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': 'Hello World!'})

@app.route('/templates')
def service():
    return render_template('home.html')

@app.route('/get')
def about():
    dictionary = {'name': 'John', 'age': 30}
    return jsonify(dictionary)

# if __name__ == '__main__':
#     app.run(debug=False , port=8080, host='0.0.0.0')