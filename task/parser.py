import json

def main():
  with open("convertcsv (1).json","rb") as file :
    data  = json.load(file)
  item = []
  new = {}
  x = 0
  for y in range(1,72) : 
    item.append(data[x]['FIELD1'])
    item.append(data[x]['FIELD2'])
    item.append(data[x]['FIELD3'])
    item.append(data[x]['FIELD4'])
    item.append(data[x]['FIELD5'])
    item.append(data[x+1]['FIELD3'])
    item.append(data[x+1]['FIELD4'])
    item.append(data[x+1]['FIELD5'])
    item.append(data[x+2]['FIELD3'])
    item.append(data[x+2]['FIELD4'])
    item.append(data[x+2]['FIELD5'])
    new[data[x]['FIELD2']] = item 
    item = []
    x = x+3
  with open("test.json","wb") as out:
    json.dump(new,out) 
  
  with open("upgeo.json","rb"):
    data = json.load(file)

  for dis in data['features']:
    try:
      if new[dis['id']] :
        dis['properties']['code'] = new[dis['id']][0]
        dis['properties']['name'] = new[dis['id']][1]
        dis['properties']['rural_avg_score'] = new[dis['id']][4]
        dis['properties']['rural_total_school'] = new[dis['id']][3]
        dis['properties']['total_score'] = new[dis['id']][7]
        dis['properties']['total_school'] = new[dis['id']][6]
        dis['properties']['urban_total_school'] = new[dis['id']][9]
        dis['properties']['urban_avg_score'] = new[dis['id']][10]
    except:
        continue
  with open("upgeo_new.json","wb") as out:
    json.dump(data,out)

if __name__ == "main" :
  main()

