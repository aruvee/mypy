import zipfile
from Pattern import Pattern
from zipfile import ZipFile
import os.path

pattern = Pattern()
print("File Extract")
entries = []
directory = "data/"
exchange = "bse"
bsezip = directory + pattern.getzipfilepath(exchange)
if os.path.exists(bsezip):
    print("bse exists")
    content = ""
    bsenewfile = open(directory + pattern.getcsvfilepath(exchange), "w")
    with zipfile.ZipFile(bsezip) as z:
        with z.open(pattern.getcsvfilepath(exchange)) as f:
            for line in f:
                content = line.decode("ascii").strip()
                content = content.replace(" ", "")
                columns = content.split(',')
                if columns[1] not in entries:
                    entries.append(columns[1])
                    bsenewfile.write(content)
                    # print(content)
                    bsenewfile.write("\n")
                else:
                    print(columns[1])
    bsenewfile.close()


exchange = "nse"
nsezip = directory + pattern.getzipfilepath(exchange)
content = ""
if os.path.exists(nsezip):
    print("nse exists")
    nsenewfile = open(directory + pattern.getcsvfilepath(exchange), "w")
    with zipfile.ZipFile(nsezip) as z:
        with z.open(pattern.getcsvfilepath(exchange)) as f:
            for line in f:
                content = line.decode("ascii").strip()
                content = content.replace(" ", "")
                nsenewfile.write(content)
                #print(content)
                nsenewfile.write("\n")
    nsenewfile.close()

exchange = "port"
portzip = directory + pattern.getzipfilepathport(exchange)
content = ""
if os.path.exists(portzip):
    print("port exists")
    portnewfile = open(directory + pattern.getcsvfilepathport(exchange), "w")
    with zipfile.ZipFile(portzip) as z:
        with z.open(pattern.getcsvfilepathport(exchange)) as f:
            for line in f:
                content = line.decode("ascii").strip()
                content = content.replace(" ", "")
                portnewfile.write(content)
                #print(content)
                portnewfile.write("\n")
    portnewfile.close()