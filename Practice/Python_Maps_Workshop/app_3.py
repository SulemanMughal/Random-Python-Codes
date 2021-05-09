import folium
map_1 = folium.Map(
    location=[45.5236, -122.6750],
    tiles='Stamen Toner',
    zoom_start=13
)
map_1.save("index_7.html")
