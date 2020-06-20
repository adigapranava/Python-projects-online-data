import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "99992929292"
  },
  "email" : {
  "hide" : "yes"
  }
}'''

info = json.loads(data)
print("Name: ",info["name"])
print("Ph no:",info["phone"]["number"])
