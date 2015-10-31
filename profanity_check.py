# read a file
# open is a built in function
import urllib

def read_text():
    file = open('fil.txt', 'r')
    read_file = file.read()
    file.close()
    profanity_check(read_file)

def profanity_check(text_to_check):
    #helps to make a connection to the above website or open a connection from a website similar to open function used above
    #helps to get data from internet
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("No curse words found")
    else:
        print("error in reading the document")
read_text()

#another website for the same purpose is http://isithackday.com/arrpi.php?text=friend
