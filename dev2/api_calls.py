from flask import Flask,jsonify,request
from services.call_services import get_all_calls,get_call_by_id,archive_call,add_notes_by_id


app = Flask(__name__)

@app.route('/')
def home():
    return("Hi")

@app.route('/calls',methods=['GET'])
def all_non_archived_calls():
    return jsonify(get_all_calls())

@app.route('/calls/<one_id>', methods=['GET'])
def one_call_by_id(one_id):
    if int(one_id)>=int("1") and int(one_id)<=int("13"):
        return jsonify(get_call_by_id(one_id)),200
    else:
        return jsonify({"id_not_found":"Wrong"}),404

@app.route('/calls/<one_id>/archive', methods=['GET'])
def archive_this_call(one_id):
    if int(one_id)>=int("1") and int(one_id)<=int("13"):
        return jsonify(archive_call(one_id)),200
    else:
        return jsonify({"Cannot arhive this call":"No existent"}),400

@app.route('/calls/<one_id>/notes',methods=['POST'])
def add_notes(one_id):
    new_notes = request.get_json()
    add_notes_by_id(one_id,new_notes)
    return jsonify({"message":"Notes added successfully"}),201



if __name__ =='__main__':
    app.run(debug=True)
