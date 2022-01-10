# Final project for ACIT4420
# Web Crawler

# External Libraries

import urllib3
import re
from bs4 import BeautifulSoup
from collections import Counter

# Save all the links and sub-link in the crawled websites
updatedUrl = []


def save_html_file():
    with open('urlWebFile.txt') as file:
        text = file.read()

    # save the links in the crawling website
    webLinks = []
    # to get the links used in the provided website for crawling
    soup = BeautifulSoup(text, 'html.parser')
    for webLink in soup.find_all(href=True):
        # saving the urls in a text file from the html file
        if str(webLink['href']).startswith("/"):
            updatedLink = webSiteAddress + str(webLink['href'])
            webLinks.append(updatedLink)
        else:
            webLinks.append(webLink['href'])

    # removing duplicate data
    for i in webLinks:
        if i not in updatedUrl:
            updatedUrl.append(i)


# User inputs for website
webSiteAddress = input("Enter the website link you want to crawl: ")

# initializing urllib3
http = urllib3.PoolManager()

# creating a text file to save downloaded url
file = open("urlWebFile.txt", "a")

# fetching the html from user given url using urllib
urlSave = http.request('GET', webSiteAddress)

# Saving the data from the url into a text file
file.write(str(urlSave.data))
file.close()
save_html_file()
print(str(len(updatedUrl)) + " sub-links has been added to urlsInText file after first iteration.")

# user input for depth of crawl
depthOfCrawl = input("Enter a number of depth to crawl between 1 to " + str(len(updatedUrl)) + " :")
if int(depthOfCrawl) <= len(updatedUrl):
    for i in range(int(depthOfCrawl)):
        # creating a text file to save downloaded url
        file = open("urlWebFile.txt", "a")

        # fetching the html from user given url using urllib
        urlSave = http.request('GET', str(updatedUrl[i]))

        # Saving the data from the url into a text file
        file.write(str(urlSave.data))
        file.close()
        save_html_file()
    print(str(len(updatedUrl)) + " sub-links has been added to urlsInText file after "+depthOfCrawl+"th interation.")
else:
    print("Provided value must be in between the fetched link numbers.")

# Saving all the fetched links into a text file
file = open('urlsInText.txt', "a")
for i in range(len(updatedUrl)):
    file.write(str(updatedUrl[i]))
    file.write("\n")
file.close()

with open('urlWebFile.txt') as file:
    text = file.read()

# Find the phone numbers inside the crawled website
phoneRegx = "\d{3}[ -]?\d{2}[ -]?\d{3}|[+47]\d{10}"
phoneNumbers = re.findall(phoneRegx, text)

# removing duplicate values from phone numbers
updatedPhoneNumber = []
for i in phoneNumbers:
    if i not in updatedPhoneNumber:
        updatedPhoneNumber.append(i)

file = open("phoneNumbers.txt", "a")
for i in range(len(updatedPhoneNumber)):
    file.write(str(updatedPhoneNumber[i]))
    file.write("\n")
file.close()
print(str(len(updatedPhoneNumber)) + " phone numbers from the crawled website has been added to phoneNumber.txt")

# Find the email addresses inside the crawled website
emailRegx = "[\w.+-]+@[\w-]+\.[\w.-]+"
emailAddresses = re.findall(emailRegx, text)

# removing duplicate values from email addresses
updatedEmail = []
for i in emailAddresses:
    if i not in updatedEmail:
        updatedEmail.append(i)

file = open("emailAddresses.txt", "a")
for i in range(len(updatedEmail)):
    file.write(str(updatedEmail[i]))
    file.write("\n")
file.close()
print(str(len(updatedEmail)) + " email addresses from the crawled website has been added to emailAddresses.txt")

# Find the comment from the crawled website
commentRegx = "<!--(.*?)-->"
comments = re.findall(commentRegx, text)

# removing duplicate data from comments
updatedComment = []
for i in comments:
    if i not in updatedComment:
        updatedComment.append(i)

file = open("comments.txt", "a")
for i in range(len(updatedComment)):
    file.write(str(updatedComment[i]))
    file.write("\n")
file.close()
print(str(len(updatedComment)) + " comments from the crawled website has been added to comments.txt")

# To find the most common 5 words
split_saved_html_file = text.split()
Counter = Counter(split_saved_html_file)
most_used_words = Counter.most_common(5)
print("Most common 5 words are used into the crawled website are below: ")
print(most_used_words)

# user defined regex to find information from the given website link
userSpecificRegx = input("Enter your desired regular expression to crawl: ")

with open('urlWebFile.txt') as file:
    text = file.read()

userDefinedRegx = str(userSpecificRegx)
datas = re.findall(userDefinedRegx, text)

file = open("userDefinedSearchFile.txt", "a")
file.write(str(datas))
file.close()
print("The data has been added into the userDefinedSearchFile.txt file.")


