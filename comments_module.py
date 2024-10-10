"""

    유튜브 영상 오픈 시 댓글 가져오는 모듈

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time



def optionSetting():
    # 브라우저 옵션 설정
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")                              # 창 띄우기 X
    options.add_argument('--mute-audio')  # 오디오 X
    options.add_argument("--disable-extensions")  # 확장 프로그램 X
    options.add_argument("--blink-settings=imagesEnabled=false")  # 이미지 로드 X
    return options


def driverSetting():
    # 드라이버로 모듈 불러온 뒤 실행
    global driver
    driver = webdriver.Chrome(options=optionSetting())
    driver.set_window_size(1000, 800)


def start():
    youtube_url = "https://www.youtube.com/watch?v=TnoDQ42UJ6U&ab_channel=MBCNEWS"
    driver.get(youtube_url)
    driver.implicitly_wait(10)
    # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    # 유튜브 링크 가져오기




global driver
driverSetting()
start()


# 프리미엄 버튼 누르기
try:
    driver.find_element(By.XPATH, '//*[@id="dismiss-button"]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
    print("pass")
except:
    pass



# 스크롤을 내리며 모든 댓글 페이지 로딩
last_scroll = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script(f"window.scrollTo(0, document.documentElement.scrollHeight);")
    driver.implicitly_wait(3)

    now_scroll = driver.execute_script("return document.documentElement.scrollHeight")
    if now_scroll == last_scroll:
        break
    last_scroll = now_scroll



html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
comments = soup.find_all("ytd-comment-thread-renderer", class_="style-scope ytd-item-section-renderer")
for comment in comments:
    comment_text = comment.find("yt-formatted-string", id="content-text").text
    try:
        print(comment_text)
    except:
        pass





# 댓글 개수 추적
comment_cnt = driver.find_element(By.XPATH, '//*[@id="count"]/yt-formatted-string/span[2]').text


for i in range(int(comment_cnt.replace(",",""))):
    pass


time.sleep(10)
# 객체 Text 불러오고 추력
elem = driver.find_element(By.XPATH, '//*[@id="content-text"]/span').text
print(elem)

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)





time.sleep(10)
# 마무리
driver.close()
