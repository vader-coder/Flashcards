filename = "es/madrigal 1 al.txt"
text = open(filename, "r").read().replace("el ", "")
open(filename, "w").write(text)