import json
lang_list,osm=[],[]
op=open('scrp.json')
file=json.load(op)
for i in file:
    if i["director"] not in osm:
        osm.append(i["director"])
        lang_list.extend(i["director"])
for k in lang_list:
    count=0
    for i in file:
        if k in i["director"]:
            count+=1   
    print(k,'=',count)