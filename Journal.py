import time
import os

# Defines an empty List to store the names of the files containing entries
titleName = []

# Creates a Directory
try:
    os.mkdir("JournalEntries")

except FileExistsError:
    pass

finally:
    os.chdir("JournalEntries")

try:
    # Opens File with list of Entry Names
    with open("titlename.txt", "r") as f:
        # Reads those Names
        entrynames = f.read()
    # Splits the names by the ","
    entrynames = entrynames.split(",")
    # Iterates through the new list of names, and append them to the list 'titleName'
    for entrytitle in entrynames:
        titleName.append(entrytitle)
# If the file titlename.txt is not found then create it.
except FileNotFoundError:
    files = open("titlename.txt", "w")
    # Closes the file
    files.close()

# Iterates through the List titleName,
for title in titleName:
    try:
# Checks if the entry has a file associated with it.
        with open(f"{title}.txt") as f:
            pass
# If entry has no file associated with it, Removes it from titleName
    except FileNotFoundError:
        titleName.remove(title)

# Defines a function called Update, which takes the list titleName as a parameter
def update(titleName):
    # Changes the list titleName into a string, connected by ',' with no space
    y = ",".join(titleName)
    # Opens titlename.txt and overwrites it's content
    with open("titlename.txt", "w") as f:
        # Replaces the overwritten content with titleName's content
        f.write(f"{y},")
# Calls Update with the titleName list as a parameter
update(titleName)

# Defines a Function called revealTitleNames
def revealTitleNames():
    print("\n")
    # Prints the list of title names
    print(f"{titleName}")
    print('\n')

    return False


# Defines a function called Exitpurge which takes the title of the entry as a paramater called x
def exitpurge(x):
    # Opens the file with the name "x" (title)
    with open(f"{x}.txt") as y:
        # Reads the file into a variable called betatxt
        betatxt = y.read()
    # Splits betatxt by "exit()" therefore removing it
    betatxt = betatxt.split("exit()")
    # Turns betatxt back into a string by joining it by an empty string
    betatxt = "".join(betatxt)
    
    # Reopens the file with the name "x" (title)
    with open(f"{x}.txt", "w") as y:
        # Overwrites the files contents with the new betatxt without the "exit()"
        y.write(betatxt)

# Defines a function called diaryentry
def diaryentry():
    # Initializes a variable called "creating" with a boolean value of True
    creating = True
    while creating:
        author = input("Who is the author of this entry?: ")
        title = input("What is the title of your Entry?: ")
        # Gets the current time of the entry
        currentTime = time.ctime()
        print("Begin your entry. Exit with exit():")
        # Initializes a variable called "writing" with a boolean value of True
        writing = True
        initialContent = input()
        # Creates/Overwrites a file with the name "title".txt
        with open(f"{title}.txt", "w") as f:
            # To the file, Writes the current time, the author, and the first line of content
            f.write(f"{currentTime}, \n{author} wrote: \n{initialContent}")
        while writing:
            content = input()
            # Continues to read lines and append them to the file
            with open(f"{title}.txt", "a") as t:
                t.write("\n")
                t.write(content)
            # Closes the file if user types "exit()"
            if "exit()" in content.lower():
                writing = False
        # Calls previously defined function exitpurge(), with the title as it's parameter  
        exitpurge(title)
        
        # Opens titlename.txt, and appends the title of the newly created file
        with open("titlename.txt", "a") as j:
            j.write(f"{title},")

        print("")
        print("Completed Successfully")
        print("Would you like to create another Entry? yes/no")
        # Appends the nameOfTitle to the list of title names
        titleName.append(f"{title}")
        ans = input()
        # Cheks to see if the answer to create another entry is yes... If so, Repeat the loop
        if ans.lower() == "yes":
            pass
        else:
            # Else, terminate the loop by setting the value to False
            print("ok\n")
            creating = False

# Defines a function called newEntryChk which checks if user wants to create a new entry
def newEntryChk():
    # Initializes a variable called running, with a value of True
    running = True
    while running:
        print("Would you like to create a new Journal Entry? yes/no: ")
        response = input()
        response = response.lower()
        if response == "yes":
            # Calls Previously defined diaryentry() function.
            diaryentry()
            return False
        elif response == "no":
            return False

        else:
            print("Invalid response.")

# Defines a function called entryshow
def entryshow():
    # Initializes a variable called running with a value of True
    running = True
    while running:
        # If the list of title names (nameOfTitle) is empty, say "No Entries Found"
        if len(titleName) == 0:
            print("No Entries Found")
            # And break out of this loop and continue with the rest of the code
            return False
        else:
            print("Here is a list of all current existing diary entries:")
            # Calls previously defined function revealTitleNames, which displays all title names
            revealTitleNames()

            print("What is the name of the entry you would like to view? Backout with exit()")
            nameOfTitle = input()
            
            if nameOfTitle.lower() == "exit()":
                return False

            # Loops through the list of title names
            for entry in titleName:
                # If the name of the entry is the same as the value user input, Read it
                if entry.lower() == nameOfTitle.lower():
                    with open(f"{entry}.txt") as f:
                        content = f.read()
                    print(f"\n{content}")
            
            if nameOfTitle not in titleName:
                print("That Entry could not be found")

            print("Would you like to view another Entry? yes/no")
            ans = input()
            if ans.lower() == "yes":
                # Repeats the loop to read another entry
                pass
            else:
                print("ok")
                # Ends the loop and continues with the code
                running = False


# Defines a function called viewEntryChk(), which checks if user wants to view an entry
def viewEntryChk():
    running = True
    while running:
        print("Would you like to view a diary entry?: yes/no")
        response = input()
        if response.lower() == "yes":
        # Calls the previously defined function entryshow() which shows the entry user wants
            entryshow()
            running = False
        elif response.lower() == "no":
            return False
        else:
            print("Invalid Response")


# Defines a function called delEntry() which deletes the requested Entry
def delEntry():
    deleting = True
    while deleting:
        # If the list of title names is empty, say "No entries Found" and end the loop
        if len(titleName) == 0:
                print("No Entries Found")
                return False
        # Calls a function which shows a list of all title names
        revealTitleNames()
        print("Please enter the name of the Entry you would like to delete. Back out with 'exit()'")
        target = input()
        if target.lower() == "exit()":
            return False
        if target not in titleName:
            print(f"{target} is not an existing Entry")
            return False

        # Loops through titleName
        for entry in titleName:
            # If the entry is the same as the requested name
            if entry.lower() == target.lower():
                # Remove it from the list of title names
                titleName.remove(entry)
                # Delete the file with that name
                try:
                    os.remove(f"{entry}.txt")
                except FileNotFoundError:
                    with open("titlename.txt", "w") as j:
                        # Overwrites the contents with the new list of titleName
                        j.write(f"{titleName},")

        # If the length of the list of title names is empty, delete the file containing said list
        if len(titleName) == 0:
                os.remove("titlename.txt")

        else:
            # Opens the file titlename.txt
            with open("titlename.txt", "w") as j:
                # Overwrites the contents with the new list of titleName
                j.write(f"{titleName},")
        print("Would you like to delete another Entry? yes/no")
        ans = input()
        if ans.lower() == "yes":
            # repeats the loop
            pass
        else:
            print("ok")
            # Ends the loop
            deleting = False


# Defines a function called delEntryChk() which checks if user wants to delete an entry
def delEntryChk():
    running = True
    while running:
        print("Would you like to delete an Entry from your journal? yes/no")
        response = input()
        if response.lower() == "yes":
            print("Noted.")
            # Calls the previously defined delEntry function
            delEntry()
            print("Completed \n")
            # Breaks out of the loop
            return True
        elif response.lower() == "no":
            # Breaks out of the loop
            running = False
        else:
            # Repeats the loop
            print("Invalid Input \n")


def main():            
    # Initializes a variable called dirunning (diary running) with a value of True
    dirunning = True
    while dirunning:
        # Function which checks if user wants to create a new entry
        newEntryChk()
        # Calls update function with the list of title names as a paramater
        update(titleName)
        # Function which checks if user wants to view an existing entry
        viewEntryChk()
        # Function which checks if user wants to delete an existing entry
        delEntryChk()
        # Function which updates the txt file and the array
        update(titleName)
        print("\nAre you Finished with your journal for now? yes/no")
        ans = input()
        if ans.lower() == "yes":
            print("See ya next time")
            # Pauses program for 3 seconds
            time.sleep(3)
            # Ends the loop, which causes the program itself to close
            dirunning = False
        else:
            # Repeats the loop
            print("Continuing... \n\n")
# Calls the function main() with no parameters
main()
