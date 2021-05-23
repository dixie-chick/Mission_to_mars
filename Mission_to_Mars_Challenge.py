#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[26]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[27]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[28]:


#set up html parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[29]:


# use .find to look inside the variable to find this specific data
slide_elem.find('div', class=_'content_title')


# ## Find the News Article

# In[ ]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


#get article summaries. There are is more than one result
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

.find() - used when we want only the first class and attribute specified

vs 

.find_all() when we want to retreive all of the tags and attributes

if we were to use .find_all() instead of .find() when pulling the summary, we would retrieve all of the summaries on the page instead of just the first one.

# ## Scrape an Image 

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url
#include the nest  img tag
#.get(src) pulls the link to the image
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

this tell BeautifulSoup to look inside the <img /> tag for an image with a class of fancybox-image. Basically we're saying, "This is where the image we want lives—use the link that's inside these tags."
# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## Scrape Mars Data 

# In[ ]:


# use read_html() to scrape a table using pandas
#1) create a new dataframe from an html table using read_html() to search and return a list of tables
df = pd.read_html('https://galaxyfacts-mars.com')[0]

#2) assign columns to the new data frame
df.columns=['description', 'Mars', 'Earth']
#3) use set_index to turn the description columns into DF index, inplace = True means updated index will remain
df.set_index('description', inplace=True)
df


# In[ ]:


#Add DF to a web application using pandas .to_html()
df.to_html()


# In[ ]:


#end the browsing session so we dont overload the computer
#browser.quit()


# ## Export to Python 

# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[30]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[31]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []



# In[32]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
#create a for loop 
for x in range(4):
    hemispheres = {}
    full_img_elm = browser.find_by_tag('h3')[x]
    full_img_elm.click()
    html = browser.html
#use BS to parse the html object
    img_soup = soup(html, 'html.parser')
    
    img_link = browser.links.find_by_text('Sample').first
    # need href code here
    img_url = img_link['href']
#use BS to find all span tags with class of "text"
    title = img_soup.find('h2', class_='title').get_text()
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()
    


# In[33]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[34]:


# 5. Quit the browser
browser.quit()


# In[ ]:




