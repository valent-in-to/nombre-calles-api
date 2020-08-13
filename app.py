from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import sqlite3

app = Flask(__name__)
CORS(app)
DATABASE = './database.sqlite3'


@app.route('/localidades', methods=['POST'])
@cross_origin()
def xd():
        try:
            if request.method == 'POST':
            req = request.get_json(force=True) 
       
            response = []
            db = sqlite3.connect(DATABASE)
            
            for i in req:
                db.row_factory = sqlite3.Row
                cur = db.cursor()
                x = cur.execute('select centroide_lat, centroide_lon from localidades where localidad_censal_id=?',(req[i],))
                y = dict(x.fetchone())
                response.append(y)

            return jsonify(response)
        except:
            pass
    return "BAD REQUEST"


if __name__ == "__main__":
    app.run()
    
