import csv
import sys

print("Welcome To The System")
# show options
id = []
name = []
midterm = []
classwork = []
csv_file = open('data.csv.csv')
# read csv file
csv_reader = csv.reader(csv_file)
# read every row of data and store item in suitable list
for lines in csv_reader:
    id.append(lines[0])
    name.append(lines[1])
    midterm.append(lines[2])
    classwork.append(lines[3])
# delete unneeded word
del id[0]
del name[0]
del midterm[0]
del classwork[0]
X=True
print("choose one of the following options :")
print ("1-Show data.\n2-Show number of students included in your data file.\n3-Show final score.\n4-Show grades.\n5-Column Statistics\n6-Show students of grade A\n7-Search by Name:\n8-Exit.")
while X:
    final_score = [None] * len(id)
    v = int(0)

    for i, j in zip(midterm, classwork):
        final_score[v] = int(i) + int(j)
        v += 1
    num = input("choosen optin:")
    if (int(num) == 1):
        # show data
        s = "{:<9} {:^20} {:^15} {:^15}".format("ID", "NAME", "MIDTERM", "CLASSWORK")
        print(s)
        for i, n, m, c in zip(id, name, midterm, classwork):

            s = "{:<9} {:^20} {:^15} {:^15}".format(i, n, m, c)
            print(s)
            print(".........................................................................................")




    if (int(num) == 2):
        # count the number of student
        for lines in csv_reader:
            id.append(line[0])
        print("number of students :", len(id))
    if (int(num) == 3):
        s = "{:<9} {:^20} {:^15}".format("ID", "NAME", "FINAL SCORE")
        print(s)

        for x, y, z, h in zip(id, name, midterm, classwork):

            s = "{:<9} {:^20} {:^15}".format(x,y,int(z)+int(h))
            print(s)
            print(".........................................................................................")
    if (int(num) == 4):
        #counting grade
        s = "{:<9} {:^20} {:^15}".format("ID", "NAME", "GRADE")
        print(s)
        for i,j,x,y in zip(midterm,classwork,name,id):
            if((int(i)+int(j))<=100 and (int(i)+int(j))>=90 ):
                s = "{:<9} {:^20} {:^15}".format(y,x, "A")
                print(s)
                print(".........................................................................................")
            elif ((int(i)+int(j))<90 and (int(i)+int(j))>=75):
                s = "{:<9} {:^20} {:^15}".format(y,x, "B")
                print(s)
                print(".........................................................................................")
            elif ((int(i)+int(j))<75 and (int(i)+int(j))>=60):
                s = "{:<9} {:^20} {:^15}".format(y,x, "C")
                print(s)
                print(".........................................................................................")
            elif ((int(i)+int(j))<60 and (int(i)+int(j))>=50):
                s = "{:<9} {:^20} {:^15}".format(y,x, "D")
                print(s)
                print(".........................................................................................")
            elif ((int(i)+int(j))<50):
                s = "{:<9} {:^20} {:^15}".format(y,x, "F")
                print(s)
                print(".........................................................................................")
    if (int(num) == 5):

        print("min: ", min(final_score))
        print("max: ", max(final_score))
        s = int(0)
        for i in range(len(id)):
            s += final_score[i]
        mean_of_scores = s / len(id)
        print("mean: ", mean_of_scores)
        a=0
        for i in range(len(id)):
           a=(final_score[i]-(mean_of_scores))**2
        var=a/(len(id)-1)
        print("variance: ",var)
        sd=var**0.5
        print("standard deviation: ",sd)
    if (int(num) == 6):
        print("students with grade A :")
        s = "{:<9} {:^20}".format("ID", "NAME")
        print(s)
        for i, j, x, y in zip(midterm, classwork, name, id):
            if ((int(i) + int(j)) <= 100 and (int(i) + int(j)) >= 90):

                s = "{:<9} {:^20}".format(y, x)
                print(s)
                print(".........................................................................................")
    if (int(num) == 7):
        search = input("Enter the name you want to search for or a part of it :")
        s = "{:<9} {:^20} {:^15} {:^15}".format("ID","NAME","MIDTERM","CLASSWORK")
        print(s)
        for i in range(len(id)):
            if (search in name[i]):


                s = "{:<9} {:^20} {:^15} {:^15}".format(id[i], name[i], midterm[i], classwork[i])
                print(s)
                print(".........................................................................................")

    if (int(num) == 8):
        print("thanks for using our program")
        x = False
        sys.exit()



























