from repositories.read_data import data

def short_answers():
    shorts=[]
    for call in data:
        if call['call_type']=='answered' and call['duration']<30:
            shorts.append(call)
    return shorts        

def delete_long():
    long_talks=[]
    for call in data:
        if call['duration']>50 and call['call_type']=='answered':
            long_talks.append(call)
            data.remove(call)
    return long_talks 