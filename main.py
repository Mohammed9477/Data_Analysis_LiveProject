import csv
file = open(r"C:\Users\moham\Downloads\Emissions.csv")
mydict = {}
reader = csv.reader(open(r"C:\Users\moham\Downloads\Emissions.csv"))
for i, rows in enumerate(reader):
        if i == 0: continue
        k = rows[0]
        v = rows[1]
        if not k in mydict:
            mydict[k] = [v]
        else:
            mydict[k].append(v)
print (mydict)
print("the first day of the project : 28/4/2022")
