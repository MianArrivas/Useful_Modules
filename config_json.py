import json, codecs

coordenates = [[(0, 0), (1, 1), (2, 2)], [(3, 3), (4, 4), (5, 5)]]

other_values = [10, 15]

coord = {'rectangles': coordenates, 'values': other_values}

json_string = json.dumps(coord)

print(f"Json_string: {json_string}")

json_coords = json.loads(json_string)
print(f"Json_coords: {json_coords['rectangles'][1]}")

with open('config.json', 'wb') as f:
    json.dump(json_string, codecs.getwriter('utf-8')(f), ensure_ascii=False)
with open('config.json') as fr:
    data = json.load(fr)
    data = json.loads(data)
    print(data['values'][0])