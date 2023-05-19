from selenium import webdriver
from bs4 import BeautifulSoup
import mysql.connector
import MySQLdb


driver = webdriver.Chrome()
conn = mysql.connector.connect(host='localhost',
                               database='test_data',
                                user='root',
                                password='amritesh3011',
                                autocommit=True)

# result=cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS jobs (
#         title TEXT,
#         organization TEXT,
#         type TEXT,
#         description TEXT,
#         proc TEXT,
#         apply TEXT

#     )
#     """
# )

cursor = conn.cursor()
lst=["https://grad.illinois.edu/clearinghouse/writers-workshop-teaching-assistantship-graduate-writing-consultant-0",
     "https://grad.illinois.edu/clearinghouse/writers-workshop-teaching-assistantship-graduate-writing-consultant",
     "https://grad.illinois.edu/clearinghouse/writers-workshop-teaching-assistantship-science-writing-consultant",
     "https://grad.illinois.edu/clearinghouse/pre-professional-graduate-assistant-counseling-center-emphasis-alcohol-and-other-0",
     "https://grad.illinois.edu/clearinghouse/pre-professional-graduate-assistant-pga-counseling-center-emphasis-programming-0",
     "https://grad.illinois.edu/clearinghouse/pre-professional-graduate-assistant-counseling-center-emphasis-alcohol-and-other-drug",
     "https://grad.illinois.edu/clearinghouse/pre-professional-graduate-assistant-counseling-center-emphasis-therapeutic-services",
     "https://grad.illinois.edu/clearinghouse/pre-professional-graduate-assistant-pga-counseling-center-emphasis-programming",
     "https://grad.illinois.edu/clearinghouse/pre-professional-graduate-assistant-pga-counseling-center-emphasis-programming-queers",
     "https://grad.illinois.edu/clearinghouse/pre-professional-graduate-assistant-counseling-center-emphasis-psychological-trauma",
     "https://grad.illinois.edu/clearinghouse/outreach-and-prevention-services-graduate-assistant",
     "https://grad.illinois.edu/clearinghouse/eating-disorders-outreach-graduate-assistant",
     "https://grad.illinois.edu/clearinghouse/counseling-center-paraprofessional-program-ppga",
     "https://grad.illinois.edu/clearinghouse/teaching-assistant-las-291292-global-perspectives-course",
     "https://grad.illinois.edu/clearinghouse/beckwith-residential-support-services-disability-liaison"]
for i in lst:
    print(i)
    driver.get(i)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extract the job title

    title_element = soup.find('title')
    title = title_element.text

    # Extract the job details
    job_details = soup.select('div.field-items')

    # Extract the organization
    organization = job_details[0].select_one('div.field-item').text.strip()

    # Extract the job type
    job_type = job_details[1].select_one('div.field-item').text.strip()

    # Extract the percent
    percent = job_details[2].select_one('div.field-item').text.strip()

    # Extract the description
    description = job_details[3].select_one('div.field-item').text.strip()

    # Extract the application procedure
    application_procedure = job_details[4].select_one('div.field-item').text.strip()

    # Extract the contact name
    contact_name = job_details[5].select_one('div.field-item').text.strip()

    # Extract the contact email
    contact_email = job_details[6].select_one('div.field-item a').text.strip()

    # Print the results
    # print('Job Title:', title)
    # print('Organization:', organization)
    # print('Job Type:', job_type)
    # print('Percent:', percent)
    # print('Description:', description)
    # print('Application Procedure:', application_procedure)
    # print('Contact Name:', contact_name)
    # print('Contact Email:',contact_email)


    #insert the data into the table
    sql="INSERT INTO jobs (title,organization,type,description,proc,apply) VALUES (%s, %s, %s, %s, %s, %s)"
    result=cursor.execute(sql,(title,organization,job_type, description, application_procedure, contact_email))
    print(result)

# close the connection
conn.close()
