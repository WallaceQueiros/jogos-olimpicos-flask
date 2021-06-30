json_path = "../static/data/competicoes.json"

def read():
    with open(json_path, 'r') as f:
        return json.load(f)['competicoes']
         

def write(competicoes):
    with open(json_path, 'w') as f:
        json.dump({'competicoes': competicoes}, f)
