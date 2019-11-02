# r = '''
# [{
#     "name": "Bob",
#     "gender": "male",
#     "birthday": "1992-10-18"
# }, {
#      "name": "Selina",
#     "gender": "female",
#     "birthday": "1995-10-18"
# }]
# '''
# import json
# print(type(r))
# data = json.loads(r)
# print(data)
# print(type(data))
# print(data[0]['gender'])
# print(data[1].get('gender'))

data = [{
    'name': '博士',
    'gender': 'male',
    'birthday': '1992-10-18'
}]

import json

with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, ensure_ascii=False))