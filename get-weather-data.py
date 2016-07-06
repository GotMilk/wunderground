import urllib.request
from bs4 import BeautifulSoup

# create/open a file called wunder.txt, which will be comma-delimited
f = open('wunder-data.txt', 'w')

# iterate through months and days
for m in range(1, 13):
    for d in range(1, 32):

        # check if end of month has been reached
        if(m == 2 and d > 28):
            break
        elif(m in [4, 6 ,8, 9, 11] and d > 30):
            break

        # open the url
        timestamp = '2015' + str(m) + str(d)
        print("Getting data for " + timestamp)
        url = "https://www.wunderground.com/history/airport/CWWA/2015/" + str(m) + "/" + str(d) + "/DailyHistory.html"
        page = urllib.request.urlopen(url)

        # get the max temperature for the day
        soup = BeautifulSoup(page)

        # dayTemp = soup.body.wx-value.string
        dayTemp = soup.findAll(attrs = {"class":"wx-value"})[1].string

        # format month for timestamp
        if len(str(m)) < 2:
            mStamp = '0' + str(m)
        else:
            mStamp = str(m)

        # format day for timestamp
        if len(str(d)) < 2:
            dStamp = '0' + str(d)
        else:
            mStamp = str(d)

        # build timestamp
        timestamp = '2015' + mStamp + dStamp

        # write timestamp and temperature to file
        f.write(timestamp + ',' + dayTemp + '\n')

# done getting data! close file
f.close()
