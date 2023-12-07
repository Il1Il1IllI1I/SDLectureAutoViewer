from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
from bs4 import BeautifulSoup

# 웹드라이버 초기 설정
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path='C:\\Users\\USER\\Downloads\\chromedriver_win32\\chromedriver.exe', options=options)

# 로그인 페이지 열기
login_url = "http://www.sdulife.com/99_Etc/DupLogin.asp?Referrer=stud.sdulife.com/Frameset/Main.asp"
driver.get(login_url)
time.sleep(1)
input("공인인증서, PC등록 완료되면 엔터키")

# 과목 코드
subject_codes = ['51', '13', '52', '54', '55', '56', '57']
result_list = []

# 과목 코드 별로 강의 정보 파싱 및 저장
def fetch_lecture_info(code):
    url = f'http://stud.sdulife.com/02_Lecture/Lecture/Lecture_Chapter.asp?YearHaki=20232&RecSeq=6&SubjCode=C000{code}&Icon=List'
    driver.get(url)
    time.sleep(3)
    html = BeautifulSoup(driver.page_source, 'html.parser')
    txt = html.find_all(class_='text1')
    txt_list = [i.text for i in txt]
    return [int(re.search(r'(\d+)\s분', item).group(1)) for item in txt_list if re.search(r'(\d+)\s분', item)]

# 과목별 강의 시청
def view_lecture(code, durations):
    url = f'http://stud.sdulife.com/02_Lecture/Lecture/Lecture_Chapter.asp?YearHaki=20232&RecSeq=6&SubjCode=C000{code}&Icon=List'
    driver.get(url)
    time.sleep(3)
    for i, duration in enumerate(durations):
        try:
            element = driver.find_element(By.XPATH, f'//*[@id="Menu_js_img"]/div[3]/table[2]/tbody[{i+1}]/tr/td[4]/div/a/span/img')
            element.click()
            time.sleep((duration + 1) * 60)
        except Exception as e:
            print(f"내부 루프 오류: {e}")

# 메인 프로그램 실행
for code in subject_codes:
    durations = fetch_lecture_info(code)
    result_list.append(durations)
    view_lecture(code, durations)

print("모든 과정이 완료되었습니다.")
