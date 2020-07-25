from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import BeautifulSoupExtractOnePage as BS

def click_all_links():
#_--------------------------------WORKS Only If you have Good Internet Connection otherwise chromedriver crahses-----------------
	#get only the links from job title
	links = [link.find_element_by_css_selector('a').get_attribute('href') for link in driver.find_elements_by_class_name('job-title-text')]
	
	print(links)
	BS.links(links)
	driver.close()
	# for link in links:
	# 	driver.get(link) #click on the link

	# 	#wait until loaded
	# 	try:
	# 		element_present = EC.presence_of_all_elements_located
	# 		WebDriverWait(driver, 50).until(element_present)
	# 	except TimeoutException:
	# 		print("Timed out waiting for page to load")
	# 	finally:
	# 		print("Page loaded")
		
#-----------------clicks each link----------------------------






#chrome_path ="C:\PC\ML\SUBLIME\Scraping\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(chrome_path)

driver.get("https://jobs.bdjobs.com/jobsearch.asp?fcatId=8")
page=0

try:
	page=page+1
	print("Page ",page," Entering\n")
	element_present = EC.presence_of_all_elements_located((By.CLASS_NAME, 'job-title-text'))
	WebDriverWait(driver, 50).until(element_present)
except TimeoutException:
	print("Timed out waiting for page to load")
finally:
	print("Page ",page," loaded")

click_all_links()
