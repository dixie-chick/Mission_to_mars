


    ###----- Find the News Article -----

    # # Use the parent element to find the first `a` tag and save it as `news_title`
    # news_title = slide_elem.find('div', class_='content_title').get_text()
    # news_title


    # #get article summaries. There are is more than one result
    # # Use the parent element to find the paragraph text
    # news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    # news_p

    #return news_title, news_p

### ---- Scrape an Image ---- 

# # Visit URL
# url = 'https://spaceimages-mars.com'
# browser.visit(url)

# # Find and click the full image button
# full_image_elem = browser.find_by_tag('button')[1]
# full_image_elem.click()

# # Parse the resulting html with soup
# html = browser.html
# img_soup = soup(html, 'html.parser')

# # Find the relative image url
# #include the nest  img tag
# #.get(src) pulls the link to the image
# img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
# img_url_rel


### ---- Scrape Mars Data ----

# use read_html() to scrape a table using pandas
#1) create a new dataframe from an html table using read_html() to search and return a list of tables
df = pd.read_html('https://galaxyfacts-mars.com')[0]

#2) assign columns to the new data frame
df.columns=['description', 'Mars', 'Earth']
#3) use set_index to turn the description columns into DF index, inplace = True means updated index will remain
df.set_index('description', inplace=True)
df


#Add DF to a web application using pandas .to_html()
df.to_html()



#end the browsing session so we dont overload the computer
browser.quit()