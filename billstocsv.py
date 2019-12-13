# first we do is for hr bills, congress nr 112
import json
import csv

with open('data/legislators/legislators_ID.csv', mode='r') as infile:
    reader = csv.reader(infile)
    dict_bioguide = {}
    dict_thomas = {}
    for person in reader:
        dict_bioguide[person[0]] = person[2]
        dict_thomas[person[1]] = person[2]

def Tidclean(Tid):
    i = 0
    while Tid[i] == "0":
        i += 1
    return Tid[i:]

# This is our module to get all the bill file paths.
from bill_paths import get_bill_file_paths

# All the bills are organized alphabetically so instead of hr1, hr2, hr3 you'll get hr1, hr10, hr100 but the order is not relevant to us.
for congress_num in range(103, 112):
    lo_bills = []
    print(congress_num)
    bill_paths = get_bill_file_paths(congress_num)

#allyears = range(1, 117) #Current year is 116
#bill_paths = {}
#for year in allyears:
 #   bill_paths[year] = get_bill_file_paths(year)
# if year

    for path in bill_paths:
        with open(path) as json_file:
            bill = json.load(json_file)
    # First check if the bill contains all the items we want for our project.
            if ("bill_id" and "official_title" and "subject_top_term" and "summary" and "sponsor") in bill.keys():
                if bill["summary"] != None:
                    dictionary = {}
                    dictionary["bill_id"] = bill["bill_id"]
    # We use the official title
                    dictionary["title"] = bill["official_title"]
    # Most bills have many subjects so we decid to only look at the top term for clarity
                    dictionary["subject"] = bill["subjects_top_term"]
                    summary_ = bill["summary"]
                    dictionary["summary"] = summary_["text"]
                    sponsor = bill["sponsor"]
                # find party in csv file from ID
                    if "thomas_id" in sponsor.keys():
                        thomas_id = sponsor["thomas_id"]
                        party = dict_thomas[Tidclean(thomas_id)]
                    if "bioguide_id" in sponsor.keys():
                        party = dict_bioguide[sponsor["bioguide_id"]]
                    dictionary["party"] = party

    # Appended to the list of bills
                lo_bills.append(dictionary)

#per bill we create a dictionary containing the following data:
#Bill id, Title, Summary
# then, we create a list of all these dictionaries

    with open('data/' + str(congress_num) + '.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter='|')
        filewriter.writerow(['bill_id', 'title', 'subject','summary', 'party'])
        for bill in lo_bills:
            filewriter.writerow([bill['bill_id'], bill['title'], bill['subject'], bill['summary'], bill['party']])
