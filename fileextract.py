import zipfile
from Pattern import Pattern
from zipfile import ZipFile
import os.path

pattern = Pattern()
print("File Extract")

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
                if "EQUITAS" not in content:
                    bsenewfile.write(content)
                    #print(content)
                    bsenewfile.write("\n")
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