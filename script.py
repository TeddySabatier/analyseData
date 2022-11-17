import pandas as pd
from datetime import datetime

excel_data=pd.read_csv('./Sample test file - Sheet1.csv')
mandatory_header=['Street', 'Zip', 'City','Last Check-In Date', 'Company' ]
continueBool=True
#Check that the required headers are in the file if not it logs and expection and stops the script
for header in mandatory_header:
    if(header not in list(excel_data.columns.values)):
        print(header ,' is not in the file.')
        continueBool=False

if continueBool:
    checkInDates=[]
    earliestCheckinDate=0
    latestCheckinDate=0
    listOfNamesOrdered=[]
    listOfUserJobsOrdered=[]
    L = excel_data.index[excel_data.isna().all(axis=1)].tolist()
    if(L!=[]):
        for val in L:
            print("The row ",val,' is empty')
    for i in excel_data.index:
        if(i not in L):
            if not pd.isnull(excel_data["Last Check-In Date"][i]):
                checkInDates.append(excel_data["Last Check-In Date"][i])
            else:
                print("The field Last Check-In Date at the row ",i," is missing." )

            FirstNameAndLastName=""
            if not pd.isnull(excel_data["First Name"][i]):
                FirstNameAndLastName=excel_data["First Name"][i]
            else:
                print("The field First Name at the row ",i," is missing." )
            if not pd.isnull(excel_data["Last Name"][i]):
                FirstNameAndLastName=FirstNameAndLastName+" "+excel_data["Last Name"][i]
            else:
                print("The field Last Name at the row ",i," is missing." )
            if(FirstNameAndLastName)!="":
                listOfNamesOrdered.append(FirstNameAndLastName)


            if not pd.isnull(excel_data["Job"][i]):
                listOfUserJobsOrdered.append(excel_data["Job"][i])
            else:
                print("The field Job at the row ",i," is missing." )
    listOfNamesOrdered=sorted(listOfNamesOrdered)
    listOfUserJobsOrdered=sorted(listOfUserJobsOrdered)
    checkInDates.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y'))
    print("List of the names ordered : ",listOfNamesOrdered)
    print("List of the jobs ordered : ",listOfUserJobsOrdered)
    print("First check in: ",checkInDates[0])
    print("Last check in: ",checkInDates[len(checkInDates)-1])


