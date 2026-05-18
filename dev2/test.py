from services.call_services import add_notes_by_id,get_all_calls,get_call_by_id,archive_call

print(get_all_calls())
print(get_call_by_id("7"))
print(archive_call("2"))
print(add_notes_by_id("3","This is a note"))

