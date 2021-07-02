import json

json_path = "static/data/competicao.json"

def read():
    with open(json_path, 'r') as f:
        return json.load(f)

def write(modalidades):
    print(f'MODALIDADES =======>{modalidades}')
    with open(json_path, 'w') as f:
        json.dump(modalidades, f)
