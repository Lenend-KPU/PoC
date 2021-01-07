import gmplot
import json

lat = []
lang = []
json_data = '{"user": 1, "route": {"id": "1","place": [{"order": "1","lat": "37.33991727961711","lang": "127.10898499766257"},{"order": "2","lat": "37.340188408836255","lang": "127.1120632688269"},{"order": "3","lat": "37.34112184451632","lang": "127.11774936994725"}]}}'

dict = json.loads(json_data)
route = dict["route"]
place = route["place"]
for pl in place:
    lat.append(float(pl.get("lat")))
    lang.append(float(pl.get("lang")))

center_lat = lat[len(lat) // 2]
center_lang = lang[len(lang) // 2]

gmapOne = gmplot.GoogleMapPlotter(center_lat, center_lang, 15)
gmapOne.scatter(lat, lang, "red", size=50, marker=False)
gmapOne.plot(lat, lang, "blue", edge_width=2.5)
gmapOne.draw("map.html")
