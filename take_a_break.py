import webbrowser 
import time 
new = 2 # opens up in a new tab 

url = "https://youtube.com"
total_breaks = 3
break_count = 0
print ("this program started on" + time.ctime())
while (break_count < total_breaks):
	time.sleep(1)
	webbrowser.open(url, new=new)
	break_count = break_count + 1
