import folium
print("Start of the mapping")
map_1 = folium.Map(location=[31.583223, 74.474485], zoom_start=17)
fg = folium.FeatureGroup(name="My Map")
coordinates = [[31.583223, 74.474485], [41.583223, 74.474485], [31.583223, 64.474485]]
for i in coordinates:
    fg.add_child(folium.Marker(location=i, popup = "Hi I'm a Marker", icon=  folium.Icon(color="red")))

map_1.add_child(fg)
map_1.save("index_10.html")
print("End of the mapping")
