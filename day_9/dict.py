ipl_dictionary={
    "RCB":"Virat kohli is capitan",
    "CSK":"MS dhoni is capitan",
    "MI":"Rohit Sharma is capitan"}
print(ipl_dictionary)

print(ipl_dictionary["MI"])

ipl_dictionary["RCB"]="King kohli is capitan"

print(ipl_dictionary)

#looping
for cricketer in ipl_dictionary:
    print(cricketer)
    print(ipl_dictionary[cricketer])

#emptying
#ipl_dictionary={}
#print(ipl_dictionary)