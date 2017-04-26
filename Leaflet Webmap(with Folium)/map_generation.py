import folium
import pandas

data = pandas.read_csv('Volcanoes-USA.txt')

map = folium.Map(location=[data['LAT'].mean(), data['LON'].mean()], zoom_start=5, tiles='Stamen Terrain')


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

for lat, lon, name, elev in zip(data['LAT'], data['LON'], data['NAME'], data['ELEV']):
    map.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev), icon_color='#000000')))


map.save(outfile='map.html')