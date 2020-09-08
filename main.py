import requests

def get_simples(url):
    r = requests.get(url)
    return r


def get_params(url, p):
    r = requests.get(url, params=p)
    return r
    

def post(url, data):
    # body => json, objeto python -> json=
    # params => parametros visiveis NÃO É SEGURO FAZER ISSO -> params=
    # data => qualquer coisa
    r = requests.post(url, json=data)
    return r


url_get = "http://localhost:5000/olamundo"
url_post = "http://localhost:5000/cadastra/usuario"

data = {
    "nome": "roger",
    "email": "roger@roger.com.br",
    "senha": "roger123"
}

response = post(url_post, data)
print(response.url)
print(response.text)
print(response.json())
