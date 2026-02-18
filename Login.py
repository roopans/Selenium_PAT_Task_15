import csv
import datetime
from turtledemo.clock import current_day

from selenium import webdriver
from selenium.webdriver.common.by import By
with open('./Files/csv_example.csv') as f:
    csv_reader = csv.DictReader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        print(row)
        # print(row['Username'])
        # print(row['Password'])
username = row['Username']
password = row['Password']
print(username)
print(password)
    #     if line_count == 0:
    #         print(f'Column names are :{", ".join(row)}')
    #         line_count += 1
    #     else:
    #         print(
    #             f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
    #         line_count += 1
    # print(f'Number of lines:  {line_count}')
#  Open the chrome browser
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
# automation with firefox browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# locate the elements
driver.implicitly_wait(60)
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(username)
driver.implicitly_wait(60)
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(password)
driver.implicitly_wait(60)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
with open('./Files/csv_example.csv', mode='w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    # writing the header
    # csv_writer.writerow(['Date', 'Time of Test', 'Name of Tester','Test Result'])
    # writing multiple rows
    row = {datetime.date:row['Date'],datetime.time():row['Time of Test'],'Tester1':row['Name of Tester'],'Pass':row['Test Result']}
    csv_writer.writerow(row)
