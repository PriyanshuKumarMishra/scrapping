import json
lang_list,osm=[],[]
op=open('scrp.json')
file=json.load(op)
for i in file:
    if i["language"] not in osm:
        osm.append(i["language"])
        lang_list.extend(i["language"])
for k in lang_list:
    count=0
    for i in file:
        if k in i["language"]:
            count+=1   
    print(k,'=',count)