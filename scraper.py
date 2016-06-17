#import requests and beautifulsoup4 using pip install
import requests
import time #so that we can add delays
from bs4 import BeautifulSoup


base_url = "http://newyork.craigslist.org/search/mis"
missed_connect_urls = []


#PART 1 - get all the urls for each missed connection pages
#-----------------------------------------------------------

#A) use requests to grab the raw data from craigslist
r = requests.get(base_url) 
# print r.content #r.content shows us raw html of page

#B) get soup using BeautifulSoup, see the content of the page in a way that is legible
soup = BeautifulSoup(r.content)
# print soup.prettify

#C) find all a tags with classname hdrlnk
urls = soup.find_all("a", class_="hdrlnk") 
# print type(urls)

#D) get the end of the link that will be each individual page
for item in urls:
  # print item
  link = item.get("href")
  full_link = "http://newyork.craigslist.org/" + link
  missed_connect_urls.append(full_link)

print missed_connect_urls



# #PART 2 - now that we have all the urls, let's get the content for each page
# #-----------------------------------------------------------

# #go through the same process as we did where we load the HTML of the page
# #do it for each page

# missed_connect_text = [] #create an empty list to hold all of our text

# for i in range(0,len(missed_connect_urls)):
#   r2 = requests.get(missed_connect_urls[i])
#   time.sleep(.05)
#   # print r2.content

#   soup = BeautifulSoup(r2.content)

#   postings = soup.find_all("section", id="postingbody")
#   for item in postings: #get the contents, without the tags on either side
#     item = item.contents
#     print item
#     missed_connect_text.append(item)

# # print missed_connect_text