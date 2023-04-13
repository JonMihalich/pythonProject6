import pprint as pp
import csv
import re


with open("adress.csv", encoding="utf8") as a:
    rows = csv.reader(a, delimiter=",")
    contacts_list = list(rows)


pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
subst = r'+7(\2)-\3-\4-\5 \6\7'

lst = []
for i in contacts_list:
    filter = ' '.join(i[0:3]).split()
    while len(filter) != 3:
        filter.append("")
    for j in range(3, 7):
        filter.append(i[j])
    lst.append(filter)


for i in lst:
    for j in lst[:-1]:
        if i[0:2] == j[0:2] and i != j:
            for k in range(7):
                if i[k]:
                    continue
                else:
                    i[k] = j[k]
            lst.remove(j)


for i in lst:
    i[5] = re.sub(pattern, subst, i[5])
pp.pprint(lst)

with open("new.csv", "w", encoding="utf8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(lst)

