from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

#chrome_path =r"E:\Code SOFTS\chromedriver.exe"

#driver = webdriver.Chrome(chrome_path)

driver.get("https://jobs.bdjobs.com/jobsearch.asp?fcatId=8")
#pagination = driver.find_elements_by_css_selector("#topPagging>ul>li")
#print(pagination.text)

#see if 1st page loads
try:
    element_present = EC.presence_of_all_elements_located((By.CLASS_NAME, 'job-title-text'))
    WebDriverWait(driver, 15).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")
# window_before = driver.window_handles[0]

# continue_link = driver.find_element_by_link_text("2")
# continue_link.click()
# window_after = driver.window_handles[1]
# driver.switch_to.window(window_after)

continue_link = driver.find_element_by_link_text("3").click()

#see if page loads
try:
    element_present = EC.presence_of_all_elements_located((By.CLASS_NAME, 'job-title-text'))
    WebDriverWait(driver, 15).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")




# window_after = driver.window_handles[0]
# driver.switch_to.window(window_after)


# for x in range(1,4):
# 	exp = driver.find_element_by_class_name("job-title-text")
# 	print(exp.text)
# 	continue_link = driver.find_element_by_link_text(str(x))
# 	continue_link.click()



#g = driver.find_elements_by_xpath("""//*[@id="jobList"]""")

#print(g)
i=1
exp = driver.find_elements_by_class_name("job-title-text")
print("page 3")
for x in exp:
# 	exp = driver.find_element_by_class_name("job-title-text")
	print(i)
	print(x.text)
	i=i+1

#Title_class = driver.find_element_by_class_name('job-title-text')




continue_link = driver.find_element_by_link_text("4").click()
try:
    element_present = EC.presence_of_all_elements_located((By.CLASS_NAME, 'job-title-text'))
    WebDriverWait(driver, 15).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded\n")


expn = driver.find_elements_by_class_name("job-title-text")
print("page 4")
for x in expn:
# 	exp = driver.find_element_by_class_name("job-title-text")
 	print(x.text)

print("HEEELLOOO")



#div.find_element_by_css_selector('a').get_attribute('href').click()


#_--------------------------------WORKS-----------------
# links = [link.find_element_by_css_selector('a').get_attribute('href') for link in driver.find_elements_by_class_name('job-title-text')]

# print(links)
# for link in links:
# 	driver.implicitly_wait(2)
# 	driver.get(link)
#-----------------clicks each link----------------------------



#for e in Title_class:
#	print(e.find_element_by_css_selector('a').get_attribute('href'))


#driver.close()

