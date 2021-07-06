date = []
time = []
logdesc = []
name = []
path = "chloe.log"

with open(path) as f:
    for line in f.readlines():
        s = line.split(" ")
        date.append(s[0])
        time.append(s[1])
        logdesc.append(s[11])

fp = open("sslvpn.csv", "w+")
a = 0
for a in range(0, len(date)):
    file = (date[a], time[a], logdesc[a])
    print(file, file = fp)
    a = a + 1



