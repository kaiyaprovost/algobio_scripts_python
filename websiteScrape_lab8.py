import urllib2

webpage = urllib2.urlopen("http://www.amnh.org/our-research/richard-gilder-graduate-school/academics-and-research/seminars-and-conferences")
weblines = webpage.readlines()
webpage.close()

import re

countTalk = 0
amnhTalk = 0

for i in range(len(weblines)):
    line = weblines[i]
    date = re.search("\d\d\-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\-\d\d",line)
    if date != None:
        countTalk += 1
        #print weblines[i:i+3]
        dateStr = date.group()
        print dateStr
        newDate = re.sub("\-16"," 2016",dateStr)
        newDate = re.sub("\-"," ",newDate)
        print newDate

        #print weblines[i+2]
        aff = weblines[i+2].find('''top">''')
        name = weblines[i+2][aff+5:].strip()
        print name,
        if name.find("American Museum") != -1:
            amnhTalk += 1

        title = weblines[i+4].find('''top">''')
        talk = weblines[i+4][title+5:].strip()
        print talk
        #title = re.search(,weblines[i+2])

        print countTalk, amnhTalk
