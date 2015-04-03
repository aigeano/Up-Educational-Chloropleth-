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

if __name__ == "main" :
  main()

