import json
from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/eq_data_4.4_4.5.geojson'
with open(filename, 'r', encoding='utf-8') as f:
    all_eq_data = json.load(f)

# запись данных в новый файл
readable_file = 'data/readable_eq_data_4.4_4.5.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']

# магнитуда, долгота, широта, местоположение
mags, lons, lats, place = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    place.append(eq_dict['properties']['title'])

for i in mags:
    if type(i) == float or type(i) == int:
        continue
    else:
        mags.remove(i)

#данные на карте
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': place,
    'marker': {
        'size': [abs(mag)*5 for mag in mags],
        'color': mags,
        'colorscale': 'plasma',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]


my_layout = Layout(title=all_eq_data['metadata']['title']+' (4.04.2024-4.05.2024)')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_1month.html')