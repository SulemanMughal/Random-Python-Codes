import folium
import pandas
data = pandas.read_csv("C:\\Program Files (x86)\\Python38-32\\Volcanoes_USA.txt")
lat = list(data["LON"])
lon =  list(data["LAT"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map_1 = folium.Map(location= [38.58, -99.09], zoom_start = 6)
fgv = folium.FeatureGroup(names="Volvanoes")

for lt, ln, el  in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [ln, lt], radius = 6,  popup = str(el)+ " m", fill_color=color_producer(el), color="grey", fill_opacity = 0.7))

fgp = folium.FeatureGroup(names="Population")
fgp.add_child(folium.GeoJson(data = open("C:\\Program Files (x86)\\Python38-32\\world.json", 'r', encoding="utf-8-sig").read(),
                            style_function = lambda x: {'fillColor': 'yellow' if x['properties']['POP2005']< 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map_1.add_child(fgv)
map_1.add_child(fgp)
map_1.add_child(folium.LayerControl())
map_1.save("Map_11.html")
