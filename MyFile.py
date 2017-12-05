class MyFile:
    def reset(self, filename):
        target = open(filename, "w")
        target.write("")
        target.close()