import utils

utils.load_json("app_data.json")

utils.write_json("shape.json", [
{
'name': 'triangle-1',
'points': [(0, 0), (10, 0), (5, 10)]
},
{
'name': 'triangle-2',
'points': [(10.2, 20.0), (30.1, 20.9), (20.3, 50.6)]
}
])

utils.load_json("shape.json")

""" Q10: La difference réside dans le fait que shape.json contient une liste de 2 objet alors que app_data.json
ne contient que un seul objet non contenu dans une liste. """


