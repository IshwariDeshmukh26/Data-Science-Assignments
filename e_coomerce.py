# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 22:08:50 2024

@author: ADMIN
"""

import bs4
from bs4 import BeautifulSoup as bs
import requests
link="https://www.amazon.in/dp/B0C7QS9M38"
page=requests.get(link)
page
page.content
## now let us parse the html page
soup=bs(page.content,'html.parser')
print(soup.prettify())
#when you parse HTML using BeautifulSoup, you are converting the 
# Find all names from the HTML
names = soup.find_all('span', class_="a-profile-name")

# Extract names, excluding non-name entries like product names and reviews
cust_names = []
for name in names:
    text = name.get_text().strip()
    # Filter: Exclude product names or review texts, keep actual customer names
    if text != "boAt Airdopes 141 ANC TWS" and len(text.split()) <= 3:  # Adjusted to keep reasonable names
        cust_names.append(text)

# Display the cleaned list of customer names
cust_names

len(cust_names)
cust_names.pop(-3)
cust_names.pop(-7)
cust_names.pop(-9)
len(cust_names)


### There are total 10 users names 
#Now let us try to identify the titles of reviews

title_rate=soup.find_all('a',class_='review-title')
tr_list = [x.text.strip() for x in title_rate]
tr_list
len(tr_list)
ratings = []
reviews = []

# Process each entry in tr_list
for i in tr_list:
    rating, review = i.split('\n', 1)
    ratings.append(rating)
    reviews.append(review)
ratings 
reviews 
rate = [int(i[0]) for i in ratings]
print(rate)
len(rate )
rate.append("")
rate.append("")
len(reviews )




# Find all reviews
reviews = soup.find_all("div", class_="a-row a-spacing-small review-data")

# Extract and clean review text
review_body = []
for review in reviews:
    text = review.get_text().strip()  # Remove leading/trailing whitespace
    cleaned_text = text.replace("Read more", "").strip()  # Remove "Read more"
    review_body.append(cleaned_text)

# Display the cleaned reviews
review_body
len(review_body )


##########################################
###convert to csv file
import pandas as pd
df=pd.DataFrame()
df['customer_names']=cust_names
df['review_title']=reviews
df['rate']=rate
df['review_body']=review_body
df
df.to_csv('C:/8-text_mining/text_mining/Amazon_shoes_reviews.csv',index=True)
########################################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
df=pd.read_csv("C:/8-text_mining/text_mining/Amazon_shoes_reviews.csv")
df.head()
df['polarity']=df['review_body'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
