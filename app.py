from flask import Flask, render_template
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://salmamnaouar01:baka%405992@cluster0.axcn93i.mongodb.net/image_generator'
mongo = PyMongo(app)


@app.route('/')
def home():
    output = []
    images = mongo.db.images.find()
    for image in images:
        image_data = {
            "url": image['image_data']['url']
        }
        output.append(image_data)
    return render_template('index.html', images=output)
@app.route('/generator')
def generator():
    return  
    
    
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8000
    )
