from functools import reduce
import os.path
data = {}

def readFile(filepath):
    if(os.path.exists(filepath)):
        with open(filepath, "r") as f:
            for line in f:
                username, artist = line.strip().split((":"))
                artistlist = artist.split(",")
                artistlist = list(map(lambda s: s.title(), artistlist))
                data[username] = sorted(artistlist)
    else:
        myfile = open("musicrecplus.txt", "w")
        myfile.close()

def writeFile(fileName, dictionary):
    """
    Input: A file name to write into and a dictionary with the data to right
    Output: Writes the data from the dictionary into the file in accordance with the format "username:Artist1,Artist2,Artist3"
    Writes from a given dictionary into the given file
    """
    file = open(fileName, "w")
    
    for person in dictionary:
        userString = person + ":" + reduce(lambda str1, str2: str1 + "," + str2, dictionary[person])
        file.write(userString + "\n")

    file.close()

def getInput():
    correctinputs = ["e", "r", "p", "h", "m", "q"]
    incorrect = True
    while incorrect:
        selection = input("Enter a letter to choose an option:"
                          "\ne - Enter preferences"
                          "\nr - Get recommendations"
                          "\np - Show most popular artists"
                          "\nh - How popular is the most popular"
                          "\nm - Which user has the most likes"
                          "\nq - save and quit\n")
        if(selection not in correctinputs):
            continue
        else:
            incorrect = False
            break
    return selection

def checkUser():
    username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
    if(username in data):
        pass
    else:
        enterPreferences(username)
    return username

def enterPreferences(username):
    artists = []
    while(True):
        artist = input("Enter an artist that you like (Enter to finish):\n")
        if(artist == ""):
            data[username] = sorted(artists)
            break
        else:
            artists.append(artist.title())
            continue

def similarprefs(randuser, currentuser):
    count = 0
    randuserartist = data[randuser]#creates a list of artists from the random user
    curruserartist = data[currentuser]
    if(randuserartist==curruserartist):#cant have the same artists
        return 0
    for artist in randuserartist:#counts similar artists
        if(artist in curruserartist):
            count += 1
    return count

def getRec(data, currentuser):
    userlist = list(data.keys())#creates a list of users from the database
    userlist.remove(currentuser)
    mostsim = 0
    mostsimuser = ""
    for user in userlist:#iterates through the list of users to find the most simliar user to the currentuser
        if("$" in user):
            continue
        numsim = similarprefs(user, currentuser)
        if(numsim==mostsim):
            continue
        elif(numsim>mostsim):
            mostsim = numsim
            mostsimuser = user

    reclist = []
    for artist in list(data[mostsimuser]):#returns a list of recommended artists not including the ones in the current users prefences
        if(artist in list(data[currentuser])):
            continue
        else:
            reclist.append(artist)
    return reclist






readFile("musicrecplus.txt")
username = checkUser()

while(True):
    selection = getInput()
    if(selection == "e"):
        enterPreferences(username)
    elif(selection == "r"):
        recs = getRec(data, username)
        print( reduce (lambda s1, s2: s1 + "\n" + s2, recs) )
    elif(selection == "p"):
        pass
    elif(selection == "h"):
        pass
    elif(selection == "m"):
        pass
    elif(selection == "q"):
        writeFile("musicrecplus.txt", data)
        break