import requests
import json
import requests
from python import python

@python.route('/api/calculate')
def calculate():
    r = requests.get("http://18.232.21.157:3000/api/queries/selectAllEvent", stream=True)
    print(r.content)
    data = json.loads(r.content)
    total = 0
    for mylist in data:
        total = total + float(mylist["ratedProductUsage"]["chargeAmount"])
    return str(total)