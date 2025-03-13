# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:35:16 2024

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

df.to_csv("c:/8-text_mining/text_mining/rotten_reviews.csv", index=True)
df

########################################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
df=pd.read_csv("c:/8-text_mining/text_mining/rotten_reviews.csv")
df.head()
df['polarity']=df['review_body'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']