from selenium import webdriver

chrome_driver_path = "C:\\Users\\marce\\Downloads\\chromedriver_win32\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463")
# price = driver.find_element_by_id("priceblock-ourprice")
# print(price.text)

driver.get("https://www.python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentantion_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentantion_link.text)

#To copy Xpath you need to go to the website and inspect the element and copy Xpath
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        "name": event_names[n].text
    }
print(events)
# Close the current tab
# driver.close()
# Close the browser
driver.quit()