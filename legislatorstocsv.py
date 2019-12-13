import csv

def Tidclean(Tid):
    i = 0
    while Tid[i] == "0":
        i += 1
    return Tid[i:]
    
with open('data/legislators/legislators-current.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    bioguide_index = your_list[0].index("bioguide_id")
    thomas_index = your_list[0].index("thomas_id")
    party_index = your_list[0].index("party")
    legis_current = []
    for row in range(len(your_list)):
        person = your_list[row]
        if len(person[thomas_index]) == 5:
            thomas_id = Tidclean(person[thomas_index])
            legis_current.append([person[bioguide_index], thomas_id, person[party_index]])
        else:
            legis_current.append([person[bioguide_index], person[thomas_index], person[party_index]])

with open('data/legislators/legislators-historical.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    bioguide_index = your_list[0].index("bioguide_id")
    thomas_index = your_list[0].index("thomas_id")
    party_index = your_list[0].index("party")
    legis_historical = []
    for row in range(1,len(your_list)):
        person = your_list[row]
        if len(person[thomas_index]) == 5:
            thomas_id = Tidclean(person[thomas_index])
            legis_historical.append([person[bioguide_index], thomas_id, person[party_index]])
        else:
            legis_historical.append([person[bioguide_index], person[thomas_index], person[party_index]])

legislators_ID = []
legislators_ID.extend(legis_current)
legislators_ID.extend(legis_historical)

import csv
with open('data/legislators/legislators_ID.csv', 'w') as outcsv:
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    for item in legislators_ID:
        writer.writerow([item[0], item[1], item[2]])
