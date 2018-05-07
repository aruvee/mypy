import requests
from Pattern import Pattern

pattern = Pattern()
directory = "data\\"
print("file download")

r = requests.get(pattern.getdownpath("bse"), stream=True)
if r.status_code == 200:
    with open(directory + pattern.getzipfilepath("bse"), 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

r = requests.get(pattern.getdownpath("nse"), stream=True)
if r.status_code == 200:
    with open(directory + pattern.getzipfilepath("nse"), 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)