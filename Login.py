import csv

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
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(username)
print(username)
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(password)
print(password)
