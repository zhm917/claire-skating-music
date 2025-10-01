from flask import Flask, render_template, jsonify

app = Flask(__name__)

Skaters = [
      {'name': 'Jessy', 'music': 'Classical Symphony'},
      {'name': 'Maya', 'music': 'Song B'},
      {'name': 'Franny', 'music': 'Song C'}
]


@app.route('/')
def home():
    return render_template('home.html', skaters=Skaters)

@app.route('/api/skaters')
def list_skaters():
     return jsonify(Skaters)

if __name__ == '__main__':
      app.run(debug=True)
