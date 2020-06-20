import json

data = ''' 	#list of dictionaries
[
{
	"id" : "001",
	"x" :"2",
	"name" : "Chuck"
},
{
	"id" : "009",
	"x" : "7",
	"name" : "Chukker"
}
]'''

info = json.loads(data)
for item in info:
	print("Name:",item["name"])
	print("Id:",item["id"])
	print("Attribute:",item["x"])
	print()
