import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html')
driver.maximize_window()


xpath_q1 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[2]/td[3]/input'
for i in range(2,10):
    xpath_q = f'/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[{i}]/td[3]/input'
    q = driver.find_element('xpath', xpath_q)
    q.send_keys('M')

xpath_q9_a = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input'
for i in range(2,22,2):
    xpath_q_a = f'/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[{i}]/td[2]/input'
    q_a = driver.find_element('xpath', xpath_q_a)
    q_a.click()

xpath_q19_a = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[3]/tbody/tr[2]/td[2]/input'
for i in range(2,10,2):
    xpath_q19_a_b = f'/html/body/div/div/div/main/div[4]/div[2]/div/form/table[3]/tbody/tr[{i}]/td[2]/input'
    q19_a_b = driver.find_element('xpath', xpath_q19_a_b)
    q19_a_b.click()

xpath_q27_a = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[5]/tbody/tr[2]/td[2]/input'
                # '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[5]/tbody/tr[4]/td[2]/input'
for i in range(2,16,2):
    xpath_q27_a_b = f'/html/body/div/div/div/main/div[4]/div[2]/div/form/table[5]/tbody/tr[{i}]/td[2]/input'
    q27_a_b = driver.find_element('xpath', xpath_q27_a_b)
    q27_a_b.click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

xpath_finish = '/html/body/div/div/div/main/div[4]/div[2]/div/form/div/p[1]/input[1]'
finish = driver.find_element('xpath', xpath_finish)
finish.click()





#
# xpath_q2 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[3]/td[3]/input'
# q2 = driver.find_element('xpath', xpath_q2)
# q2.send_keys('15')
# time.sleep(1)
#
# xpath_q9_a = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input'
# q9_a = driver.find_element('xpath', xpath_q9_a)
# q9_a.click()
# time.sleep(1)
#
# xpath_q9_a = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input'
# q9_a = driver.find_element('xpath', xpath_q9_a)
# q9_a.click()
# time.sleep(1)
#
# xpath_q9_a = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input'
# q9_a = driver.find_element('xpath', xpath_q9_a)
# q9_a.click()
# time.sleep(1)
#
# xpath_q9_a = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input'
# q9_a = driver.find_element('xpath', xpath_q9_a)
# q9_a.click()
# time.sleep(1)
#
# xpath_q19_a = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[3]/tbody/tr[2]/td[2]/input'
# q19_a = driver.find_element('xpath', xpath_q19_a)
# q19_a.click()



