from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(r"C:\\Users\\이민희\\Downloads\\chromedriver.exe") 
driver.implicitly_wait(3)
driver.get('https://www.op.gg/')

search_name = driver.find_element_by_name('userName')
search_name.send_keys('Hide on bush')
search_name.submit()

#검색 메인화면
html = driver.page_source #페이지의 elements 모두 가져오기
soup = BeautifulSoup(html, 'lxml') #BeautifulSoup 사용하기
#BeautifulSoup 객체로 변환 -> 웹문서 파싱 상태 -> 태그 별로 분해되어 태그로 구성된 트리

UserTierRankInfo = soup.find('div', class_='TierRankInfo')
print(UserTierRankInfo.text)
UserPositionStatContent = soup.find('div', class_='PositionStatContent')
print(UserPositionStatContent.text)

a = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/dl/dd[2]/a')
driver.get(a.get_attribute('href'))
driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/div/div[1]/div/div[2]').click()
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

UserChampionList = soup.find('tbody', class_='Body')
print(UserChampionList.text)