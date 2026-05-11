from repositories.read_data import data

def short_answers():
    shorts=[]
    for i in data:
        if i['call_type']=='answered' and i['duration']<30:
            shorts.append(i)
    return shorts        

def delete_long():
    long_talks=[]
    for i in data:
        if i['duration']>50 and i['call_type']=='answered':
            long_talks.append(i)
            data.remove(i)
    return long_talks 