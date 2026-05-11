from repositories.read_data import data

def get_all_calls():
    non_archived_calls = []
    for i in data:
        if i['is_archived']==False:
            non_archived_calls.append(i)
    return non_archived_calls        


def get_call_by_id(call_id):

    for i in data:
        if i['id']==call_id:
            return i
    return None    
    

def archive_call(call_id):
    for i in data:
        if i['is_archived']==False and i['id']==call_id:
            i['is_archived']=True
            return i
    return None    