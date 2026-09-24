import json

# json_string = '''
#     {   
#             "students": [
#                 {
#                     "id": 1,
#                     "name": "Tim",
#                     "age": 21,
#                     "full-time": true
#                 },
#                 {    
#                     "id": 2,
#                     "name": "Joe",
#                     "age": 33,
#                     "full-time": false
#                 }
#             ]
#     }
# '''

# data = json.loads(json_string)
# data['test'] = True

# new_json = json.dumps(data, indent=4, sort_keys=True)
# print(new_json)

json_string = '''
{
    "id":1,
    "name": "Tim",
    "age": 21,
    "full_time": true
}
'''
data = json.loads(json_string)
print(data["name"])
print(type(data))


