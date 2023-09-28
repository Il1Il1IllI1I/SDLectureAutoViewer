from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import pyautogui

def setup_webdriver(exec_path, options):
    return webdriver.Chrome(executable_path=exec_path, options=options)

def fetch_lecture_durations(driver, subject_code):
    driver.get(f'http://stud.sdulife.com/02_Lecture/Lecture/Lecture_Chapter.asp?YearHaki=20232&RecSeq=6&SubjCode=C000{subject_code}&Icon=List')
    time.sleep(3)
    html = BeautifulSoup(driver.page_source, 'html.parser')
    durations = [int(re.search(r'(\d+)\s분', text.text).group(1)) for text in html.find_all(class_='text1') if re.search(r'(\d+)\s분', text.text)]
    return durations

def play_lectures(driver, subject_code, durations):
    driver.get(f'http://stud.sdulife.com/02_Lecture/Lecture/Lecture_Chapter.asp?YearHaki=20232&RecSeq=6&SubjCode=C000{subject_code}&Icon=List')
    time.sleep(3)
    for idx, duration in enumerate(durations):
        try:
            play_button = driver.find_element(By.XPATH, f'//*[@id="Menu_js_img"]/div[3]/table[2]/tbody[{idx+1}]/tr/td[4]/div/a/span/img')
            play_button.click()
            time.sleep((duration + 1) * 60)
        except Exception as e:
            print(f"강의 재생 오류: {e}")

options = Options()
options.add_experimental_option("detach", True)
driver = setup_webdriver('C:\\Users\\USER\\Downloads\\chromedriver_win32\\chromedriver.exe', options)

login_url = "http://www.sdulife.com/99_Etc/DupLogin.asp?Referrer=stud.sdulife.com/Frameset/Main.asp"
driver.get(login_url)
time.sleep(1)
input("공인인증서, PC등록 완료되면 엔터키")

# lecture_codes = ['20', '39', '22', '03', '02', '01', '04', '31'] #Choi
lecture_codes = ['51', '13', '52', '54','55', '56', '57']  #Sung


lecture_durations = {code: fetch_lecture_durations(driver, code) for code in lecture_codes}

for code, durations in lecture_durations.items():
    play_lectures(driver, code, durations)

print("모든 과정이 완료되었습니다.")
