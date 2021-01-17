from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\\Users\\marce\\Downloads\\chromedriver_win32\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

button = driver.find_element_by_css_selector("form button")
#button = driver.find_element_by_tag_name("button")

fname.send_keys("Marcelo")
lname.send_keys("Gomes")
email.send_keys("marcelo@gomes.com")
button.click()

