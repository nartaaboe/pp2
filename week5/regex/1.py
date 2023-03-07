import re
txt = "The rain in Spain"
x = re.search("^The.*Spain%")
if x:
    print("Nice")
else:
    print("bad")