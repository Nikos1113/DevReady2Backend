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
    call = get_call_by_id(one_id)
    if call:
        return jsonify(call),200
    else:
        return jsonify({"Message":"Call is not found"}),404

@app.route('/calls/<one_id>/archive', methods=['PATCH'])
def archive_this_call(one_id):
    call = request.get_json()
    if call and call.get('is_archived'):
        archived=archive_call(one_id)
        return jsonify({"Message":"Call is archived successfully"}),200
    return jsonify({"Message":"Call is not found"}),404



@app.route('/calls/<one_id>/notes',methods=['POST'])
def add_notes(one_id):
    new_notes = request.get_json()
    add_notes_by_id(one_id,new_notes)
    return jsonify({"message":"Notes added successfully"}),201



if __name__ =='__main__':
    app.run(debug=True)
