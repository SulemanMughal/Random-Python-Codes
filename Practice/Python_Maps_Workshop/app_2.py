import folium
print("Start of the mapping")
map_1 = folium.Map(location=[45.5236, -122.6750], tiles = "CartoDB")
map_1.save("index_6.html")
print("End of the mapping")
