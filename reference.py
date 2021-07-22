import json, codecs

coordenates = [[(0, 0), (1, 1), (2, 2)], [(3, 3), (4, 4), (5, 5)]]

other_values = [10, 15]

rectangles = "rectangles"
coord = {rectangles: coordenates, 'values': other_values}

json_string = json.dumps(coord)

print(f"Json_string: {json_string}")

json_coords = json.loads(json_string)
# print(f"Json_coords: {json_coords['rectangles'][1]}")
print(f"Json_coords: {json_coords[rectangles][1]}")

valores = "Valores"
jsonValues = '{\"Valores\": \"[(1, 2), (\'Hola\',\'Mundo\')]\"}'
json_values_loads = json.loads(jsonValues)
print(f"json values: {json_values_loads['Valores']}")

with open('config.json', 'wb') as f:
    json.dump(json_string, codecs.getwriter('utf-8')(f), ensure_ascii=False)
with open('config.json') as fr:
    data = json.load(fr)
    data = json.loads(data)
    print(data['values'][0])

valor = [1]
if valor:
    print("LISTA LLENA")
else:
    print("NO hay elementos")