from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://webadmin:SSVqpk94182@node8615-advweb-24.app.ruk-com.cloud:11107/DB3table'
app.config['SQLALCHEMY_TRACK)MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

class data(db.Model):
    id = db.Column(db.String(13), primary_key=True, unique=True)
    name = db.Column(db.String(50))
    price = db.Column(db.String(25))
    

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        

        # data Schema
class dataSchema(ma.Schema):
    class Meta:
        fields =('id', 'name', 'price')

# Init Schema 
data_schema = dataSchema()
data_schema = dataSchema(many=True)

# Get All Staffs
@app.route('/data', methods=['GET'])
def get_data():
    all_data = data.query.all()
    result = data_schema.dump(all_data)
    return jsonify(result)


# Web Root Hello
@app.route('/', methods=['GET'])
def get():
    return jsonify({'ms': 'Hello DB3table'})

# Run Server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

    