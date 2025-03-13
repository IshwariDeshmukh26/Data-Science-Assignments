# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:22:03 2024

@author: ADMIN
"""
import pandas as pd
import bs4
from bs4 import BeautifulSoup as bs
import requests
url="https://www.rottentomatoes.com/tv/colin_from_accounts/s02/reviews?type=user"
#url="https://www.imdb.com/title/tt0454921/reviews/?ref_=tt_ov_ql_2"
page = requests.get(url)
page
page.content#

# let us apply html parser
soup = bs(page.content, 'html.parser')
soup
# Now the text is clean but not upto the expections
# Now let us apply prettify method
print(soup.prettify())# The text is neat and clean

# Now let us scrap the contents
# Now let us try to identify the titles of review
name = soup.find_all('a',class_="audience-reviews__name")
name
# when you will extract the web page got to all reviews rather top revews.when you
# click arrow icon and the total reviews ,there you will find span has no class
# you will have to go to parent icon i.e.a
# now let us extract the data
review_name = []
for i in range(0, len(name)):
    review_name.append(name[i].get_text())
review_name

# Output will get consists of\n
review_name[:] = [name.strip('\n') for name in review_name]
review_name
clean_names = [name.strip() for name in review_name]
print(clean_names)
len(clean_names)
# We will get 9 reviews title.

# Now let us scrap the rating
rating = soup.find_all('div',class_="audience-review-meta")
rating
# Extract only the ratings from the 'score' attribute
rate= [float(meta.find('rating-stars-group')['score']) for meta in rating]

# Print the extracted ratings
rate
len(rate)
rate.pop(-1)
len(rate)
##WE will get 9 ratings.

# Now let us scrap review body
# Find all review paragraphs
review = soup.find_all('p', class_="audience-reviews__review js-review-text")

# Extract and clean the reviews
review_body = [rev.get_text().strip() for rev in review]

# Print the cleaned reviews
review_body

len(review_body)
review_body.pop(-1)
len(review_body)

# Now we have to save the data in .csv file
import pandas as pd

df = pd.DataFrame()
df['Review_Title'] =clean_names
df['Rate'] = rate
df['Review'] = review_body
df

df.to_csv("C:/8-text_mining/text_mining/rotten_reviews.csv", index=True)
df

########################################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
df=pd.read_csv("C:/8-text_mining/text_mining/rotten_reviews.csv")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']

###########################################################

#url2 = "https://www.amazon.in/product-reviews/B08HNGK3B7"
url2="https://www.amazon.in/dp/B0C7QS9M38"
page = requests.get(url2)
page
page.content

# let us apply html parser
soup = bs(page.content,'html.parser')
soup
# Now the text is clean but not upto the expections
# Now let us apply prettify method
print(soup.prettify())
# The text is neat and clean
#When you parse the content by using beatifulSoap,you are converting the raw HTML content
#of a web page into a structure format.

# Now let us scrap the contents
# Now let us try to identify the titles of review
name = soup.find_all('span',class_="a-profile-name")
name

#As the data contains html tags,let us extract names from html tags
cust_name = []
# There are total 15 users names

#Now let us try to identify the titles of the reviews
title_rate=soup.find_all('span',class_="a-letter-space")
t_list=[x.text.strip()for x in title_rate]
len(t_list)
t_list.pop(-1)
t_list.pop(-1)
t_list.pop(-1)
t_list.pop(-1)
len(t_list)
ratings=[]
reviews=[]


#Enter each data in t_list
for i in t_list:
    rating,review=i.split('/n',1)
    ratings.append(rating)
    ratings.append(review)
rating
reviews
rate=[int(i[0])for i in ratings]
print(rate)
len(rate)
len(reviews)


# Now let us scrap review body
review = soup.find_all('div', class_="a-row a-spacing-small review-data")
review
# We got the data
review_body = []
for i in range(0, len(review)):
    review_body.append(review[i].get_text())
review_body
review_body=[review.strip('\n\n')for review in review_body]
review_body
len(review_body)

#Convert to csv file
df = pd.DataFrame()
df['custemer_name']=cust_name
df['review_Title'] = review
df['rate'] = rate
df['review_body'] = review_body
df

df.to_csv("c:/8-text_mining/text_mining/Amazon_shoes_reviews.csv", index=True)
df

#sentiment analysis
import pandas as pd
from textblob import TextBlob
df=pd.read_csv("C:/8-text_mining/text_mining/Amazon_shoes_reviews.csv")
df.head()
df['polarity']=df['review_body'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)

#####################################################
##Boat Eardopes
import bs4
from bs4 import BeautifulSoup as bs
import requests

link="https://www.boat-lifestyle.com/products/rockerz-450-pro"
page=requests.get(link)
page
page.content
## now let us parse the html page
soup=bs(page.content,'html.parser')
print(soup.prettify())
#when you parse HTML using BeautifulSoup, you are converting the 
#raw HTML content of a web page into a structured format, 
#like a tree, where you can easily locate and manipulate individual 
#elements (such as tags, attributes, or text).

#page.content=> provides the raw HTML content,
#while soup.prettify()=> offers a formatted, human-readable version of the parsed HTML content.

## now let us scrap the contents
names=soup.find_all('span',class_="jdgm-rev__author")
names
### but the data contains with html tags,let us extract names from html tags
cust_names=[]
for i in range(0,len(names)):
    cust_names.append(names[i].get_text())
    
cust_names
len(cust_names)
#cust_names.pop(-1)
#len(cust_names)


### There are total 6 users names 
#Now let us try to identify the titles of reviews

title=soup.find_all('b',class_="jdgm-rev__title")
title
# when you will extract the web page got to all reviews rather top revews.when you
# click arrow icon and the total reviews ,there you will find span has no class
# you will have to go to parent icon i.e.a
#now let us extract the data
review_titles=[]
for i in range(0,len(title)):
    review_titles.append(title[i].get_text())
review_titles

len(review_titles)
##now let us scrap ratings
rating=soup.find_all('span',class_="jdgm-rev__title")
rating
###we got the data
ratings = [int(span['data-score']) for span in soup.find_all('span', {'class': 'jdgm-rev__rating'})]

# Print the ratings
print(ratings)

len(ratings)



## now let us scrap review body
reviews=soup.find_all("div",class_="jdgm-rev__body")
reviews
review_body=[]
for i in range(0,len(reviews)):
    review_body.append(reviews[i].get_text())
review_body
review_body=[ reviews.strip('\n\n')for reviews in review_body]
review_body
len(review_body)

##########################################
###convert to csv file
import pandas as pd
df=pd.DataFrame()
df['customer_names']=cust_names
df['review_title']=review_titles
df['rate']=ratings
df['review_body']=review_body
df
df.to_csv('C:/8-text_mining/text_mining/Boat_ear_reviews.csv',index=True)
########################################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
df=pd.read_csv("C:/8-text_mining/Text_mining/Boat_ear_reviews.csv")
df.head()
df['polarity']=df['review_body'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']


#########################################

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
df.to_csv('C:\Assignments DS\Web Scrapping\Amazon_shoes_reviews.csv',index=True)
########################################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
df=pd.read_csv("C:\Assignments DS\Web Scrapping\Amazon_shoes_reviews.csv")
df.head()
df['polarity']=df['review_body'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']