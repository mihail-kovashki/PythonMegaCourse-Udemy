import folium
import pandas

data = pandas.read_csv('Volcanoes-USA.txt')

map = folium.Map(location=[data['LAT'].mean(), data['LON'].mean()], zoom_start=5, tiles='Mapbox bright')


def color(elev):
    minimum_elev = int(data['ELEV'].min())
    step = int((max(data['ELEV'])-min(data['ELEV']))/3)
    if elev in range(minimum_elev, minimum_elev+step):
        col = 'green'
    elif elev in range(minimum_elev+step, minimum_elev+step*2):
        col = 'orange'
    else:
        col = 'red'
    return col

volcanoes_group = folium.FeatureGroup(name='Volcanoes')

for lat, lon, name, elev in zip(data['LAT'], data['LON'], data['NAME'], data['ELEV']):
    volcanoes_group.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev), icon_color='#000000')))

map.add_child(volcanoes_group)

map.add_child(folium.GeoJson(data=open('world_population.json'),
                             name='World Population',
                             style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<50000000 else 'red'}))

map.add_child(folium.LayerControl())

map.save(outfile='unempl_map.html')