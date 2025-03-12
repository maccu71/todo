from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Read from environment variable
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['my_database']
collection = db['my_collection']

@app.route('/items')
def get_items():
    items = list(collection.find())
    return render_template('items.html', items=items, title='ITEMS!')

@app.route('/')
def home():
    return render_template('home.html', title='HOME!')

@app.route('/about')
def about():
    return render_template('about.html', title='ABOUT')

@app.route('/update', methods=['POST','GET'])
def update():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        if not name or not description:
            return "Missing 'name' or 'description' parameter!", 400
        new_item = {'name': name, 'description': description}
        collection.insert_one(new_item)
        return redirect(url_for('get_items'))
    if request.method == 'GET':
        return render_template('request.html', title='REQUEST')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
