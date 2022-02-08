from selenium import webdriver
search_string = input("input the Url or srting you want to search for:")
search_string = search_string.replace(' ','+')
browser = webdriver.Safari('Safaridriver')
for i in range(1):
	matched_elements =  browser.get("http://www.google.com/search?q=" + search_string + "&start=" + str(i))