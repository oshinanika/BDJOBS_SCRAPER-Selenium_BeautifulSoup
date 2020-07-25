# import libraries
import pandas as pd
import urllib.request as urllib
from bs4 import BeautifulSoup

def BS_1pg(links, dataframe):



	
	for link in links:
		quote_page = link
		# query the website and return the html to the variable ‘page’
		page = urllib.urlopen(quote_page)
		soup = BeautifulSoup(page, 'html.parser')
		punctuation = " "  # for sentences without fullstop


		# ----------------------------JOB SUMMARY col-md-4------------------
		job_sum = soup.find('div', attrs={'class': 'panel-body'})
		#print(job_sum)
		j = 0

		#print('-' * 10 + "SUMMARY" + "-" * 10)
		#extract the summary (maximum 9 datas in a summary)

		sum_all_data = job_sum.find_all('h4')  # get all the h4 tags from summary
		# Publishe on
		try:
			if(sum_all_data[j].find('strong').text == "Published on:"):
				publish_date=sum_all_data[j].find('strong').findNextSibling(text=True).strip()  # findNextSibling= text after the strong tag
				j+=1
			else:
				raise NameError
		except NameError:
			publish_date = 'None'


		#vacancy
		try:
			if(sum_all_data[j].find('strong').text == "Vacancy:"):
				vacancy = sum_all_data[j].find('strong').findNextSibling(text=True).strip()
				j+=1
			else:
				raise NameError
		except NameError:
			vacancy = 'None'

		#employment status
		try:
			if(sum_all_data[j].find('strong').text == "Employment Status:"):
				status = sum_all_data[j].find('strong').findNextSibling(text=True).strip()
				j+= 1
			else:
				raise NameError
		except NameError:
			status = 'None'

		#experience
		try:
			if(sum_all_data[j].find('strong').text == "Experience:"):
				exp = sum_all_data[j].find('strong').findNextSibling(text=True).strip()
				j+= 1
			else:
				raise NameError
		except NameError:
			exp = 'None'

		#gender
		try:
			if(sum_all_data[j].find('strong').text == "Gender:"):
				gender = sum_all_data[j].find('strong').findNextSibling(text=True).strip()
				j+= 1
			else:
				raise NameError
		except NameError:
			gender = 'None'

		#age
		try:
			if(sum_all_data[j].find('strong').text == "Age:"):
				age = sum_all_data[j].find('strong').findNextSibling(text=True).strip()
				j+= 1
			else:
				raise NameError
		except NameError:
			age = 'None'


		#job location
		try:
			if(sum_all_data[j].find('strong').text == "Job Location:"):
				location = sum_all_data[j].find('strong').findNextSibling(text=True).strip()
				j+= 1
			else:
				raise NameError
		except NameError:
			location = 'None'


		#salary
		try:
			if(sum_all_data[j].find('strong').text == "Salary:"):
				salary = sum_all_data[j].find('strong').findNextSibling(text=True).strip()
				j+= 1
			else:
				raise NameError
		except NameError:
			salary = 'None'

		#deadline
		try:
			if(sum_all_data[j].find('strong').text == "Application Deadline:"):
				deadline = sum_all_data[j].find('strong').findNextSibling(text=True).strip()
				j+= 1
			else:
				raise NameError
		except NameError:
			deadline = 'None'

		#print(publish_date,vacancy,status,exp,gender,age,location,salary, deadline)
		#print('-'*10+"SUMMARY"+"-"*10)
		#print("\n")
		#----------------------------------JOB SUMMARY-----------------------


		#---------------------------------JOB DETAILS------------------------

		#FULL JOB: Take out the <div> of col-md-8 and get it
		job_data = soup.find('div', attrs={'class': 'col-md-8'})

		# get the job title class
		try:
			job_title = job_data.find('h4', attrs={'class':'job-title'})
			job_title = job_title.text
		except:
			job_title = 'None'


		# get the company name class
		try:
			company_name = job_data.find('h2', attrs={'class':'company-name'})
			company_name=company_name.text
		except:
			company_name = 'None'

		# get the job description class (both job context and job responsibilities are together)
		job_des_multi=job_data.findAll('div', attrs={'class':'job_des'})
		len_job_desc_multi = len(job_des_multi)

		job_desc_full=''
		for count in range(len_job_desc_multi):
			job_resp= job_data.findAll('div', attrs={'class':'job_des'})[count].find('ul').findAll("li")#job context/responsbilties as list
			if(job_resp!=[]):	
				i=0
				for resp in job_resp:
					job_desc_full=job_desc_full+job_resp[i].text.strip()+punctuation 
					i=i+1
			else:
				job_desc_full=job_desc_full+job_data.findAll('div', attrs={'class':'job_des'})[count].find('ul').text.replace('N/A','').strip()+punctuation
		


		# get education & exp  requirements (both in same class)
		edu_exp_req = job_data.findAll('div', attrs={'class':'edu_req'})
		try:
			# get the job title class
			edu_req_list = edu_exp_req[0].find('ul').findAll('li')
			edu_req=""
			i=0
			for req in edu_req_list:
				edu_req=edu_req+edu_req_list[i].text.strip()+punctuation
				i=i+1
		except:
			edu_req = 'None'


		#get exp requirements
		try:
			exp_req_list = edu_exp_req[1].find('ul').findAll('li')
			exp_req=""
			i=0
			for req in exp_req_list:
				exp_req=exp_req+exp_req_list[i].text.strip()+punctuation
				i=i+1
		except:
			exp_req = 'None'


		#get the additional requirements
		try:
			# get the job title class
			job_req_list = job_data.find('div', attrs={'class':'job_req'}).find('ul').findAll('li')
			add_job_req=""
			i=0
			for req in job_req_list:
				add_job_req=add_job_req+job_req_list[i].text.strip()+punctuation #all job resposibilities as a paragraph
				i=i+1
		except:
			add_job_req = 'None'

		#get the Benefits
		try:
			# get the job title class
			ben_list = job_data.find('div', attrs={'class':'oth_ben'}).find('ul').findAll('li')
			benefits=""
			i=0
			for ben in ben_list:
				benefits=benefits+ben_list[i].text.strip()+punctuation #all job resposibilities as a paragraph
				i=i+1
		except:
			benefits = 'None'

		#print("JOB TITLE:",job_title,"company-name:",company_name,"JOB DESCriptionnnnn:",job_desc_full,"Edu Req:_",edu_req,"_","EXP Req:_",exp_req,"_\n","Additional Job Req:_",add_job_req,"_","Benefits:_",benefits,"_")

		#save  dats in to a dataframe
		dataframe = dataframe.append({"JOB_TITLE":job_title, "COMPANY":company_name, "VACANCY":vacancy, "AGE":age,
			"GENDER":gender, "LOCATION":location, "EMPLOYEMENT_STATUS":status, "SALARY":salary,
			"JOB_DESCRIPTION":job_desc_full, "EDUCATION_REQUIREMENTS":edu_req, "EXPERIENCE":exp, "EXPERIENCE_REQUIREMENTS":exp_req,
			"ADDITIONAL_REQUIREMENTS":add_job_req, "BENEFITS":benefits, "PUBLISHED_DATE":publish_date, "DEADLINE":deadline},
			ignore_index=True)

		print(job_title)
	#save the dataframe to csv
	dataframe.to_csv("G:\ML\SUBLIME\Scraping\BDJOBS SCRAPING\BDJOBS_DATA.csv",index=False, mode='a')
	print("dataframe")



def links(links):
	links = links
	dataframe = pd.DataFrame(columns=["JOB_TITLE", "COMPANY", "VACANCY", "AGE",
			"GENDER", "LOCATION", "EMPLOYEMENT_STATUS", "SALARY",
			"JOB_DESCRIPTION", "EDUCATION_REQUIREMENTS", "EXPERIENCE", "EXPERIENCE_REQUIREMENTS",
			"ADDITIONAL_REQUIREMENTS", "BENEFITS", "PUBLISHED_DATE", "DEADLINE"])
	
	BS_1pg(links, dataframe)