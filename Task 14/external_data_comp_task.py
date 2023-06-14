#used https://stackoverflow.com/questions/55251494/i-want-to-create-a-program-that-reads-data-from-a-text-file-and-print-it-out-in to help code
#empty lists to append data onto
names = []
birthdays = []

file = open("DOB.txt", "r+")
# .readlines() splits the text file into a list with each line as an item
data = file.readlines()

#iterates over the data list, splits the lines into further separate lists, appends the names and birthdates in their respective lists
for line in data:
    parts = line.split()
    names.append(parts[:2])
    birthdays.append(parts[2:])

file.close



print("Name")
#enumerate gives a count of the current iteration
for i, name in enumerate(names, start=1):
    print("{}. {}".format(i, " ".join(name)))

print("Birthdate")

for i, birthd in enumerate(birthdays, start=1):
    print("{}. {}".format(i, " ".join(birthd)))