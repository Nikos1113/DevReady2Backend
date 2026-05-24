from repositories.read_data import data

def get_all_calls():
    non_archived_calls = []
    for call in data:
        if call['is_archived']==False:
            non_archived_calls.append(call)
    return non_archived_calls        


def get_call_by_id(call_id):

    for call in data:
        if call['id']==call_id:
            return call
    return None    
    

def archive_call(call_id):
    for call in data:
        if not call['is_archived'] and call['id']==call_id:
            call['is_archived']=True
            return call
    return None  

def add_notes_by_id(call_id,notes):
    for call in data:
        if call['id']==call_id:
            call['notes'] = (notes) 
            return call
    return None     