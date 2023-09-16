# SDLectureAutoViewer
# 🎓 SDULectureAutoViewer: 성균관대학교 자동 강의 시청 도우미

## 🌈 소개

🌟 **SDULectureAutoViewer**는 성균관대학교의 강의를 자동으로 시청해주는 놀라운 파이썬 스크립트입니다. 지금부터 새로운 강의 시청 경험을 시작해보세요!

---

## 🎨 주요 기능

1. 📝 **과목별 강의 정보 수집**: 각 과목의 강의 정보를 자동으로 수집합니다.
2. 🎥 **강의 자동 시청**: 수집된 정보를 바탕으로 강의를 자동으로 시청합니다.

---

## 🛠️ 사용된 기술

- 🐍 **Python**: 프로그래밍 언어
- 🌐 **Selenium**: 웹 브라우저를 자동으로 제어할 수 있게 도와주는 라이브러리
- 🍲 **BeautifulSoup**: 웹 페이지의 내용을 쉽게 가져올 수 있게 도와주는 라이브러리

---

## 📥 설치 방법

### 1️⃣ Python 설치

👉 [Python 공식 페이지](https://www.python.org/downloads/)에서 최신 버전의 Python을 설치합니다.

### 2️⃣ 필요한 라이브러리 설치

👉 터미널을 열고 아래 명령어를 실행합니다.

🚀 사용 방법
1️⃣ 스크립트 실행
👉 터미널에서 아래 명령어를 실행합니다.

bash
Copy code
python SDULectureAutoViewer.py
2️⃣ 인증 완료
👉 공인인증서와 PC등록을 완료한 후, 터미널에 나타난 메시지를 따라 엔터키를 누릅니다.

3️⃣ 자동 강의 시청 시작!
👉 이제부터 스크립트가 자동으로 강의를 시청해 줍니다. 편안한 의자에 앉아서 커피 한 잔 하세요 ☕

❗ 주의사항
🚫 이 스크립트는 학습 목적으로만 사용되어야 하며, 사용자는 이 스크립트를 사용함으로써 발생하는 모든 결과에 대한 책임을 집니다.

📝 라이선스
📜 이 프로젝트는 MIT 라이선스 하에 있습니다. 자세한 내용은 LICENSE 파일을 참조하세요.

📚 추가 정보
📖 코드 설명: 이 스크립트는 Python 언어로 작성되었으며, Selenium과 BeautifulSoup 라이브러리를 사용하여 웹 브라우저를 제어하고 웹 페이지의 내용을 파싱합니다.
🌟 어떻게 작동하는지: 스크립트는 성균관대학교의 강의 페이지에 로그인한 후, 설정된 과목 코드에 따라 각 과목의 강의를 찾아 시청합니다. 강의의 길이는 자동으로 계산되어, 각 강의가 끝나면 다음 강의로 넘어갑니다.

---

🎓 SDLectureAutoViewer 🎓
📌 목차
설명
사용법
코드 구조
주의사항
📜 설명
이 스크립트는 Selenium과 BeautifulSoup를 사용하여 www.sdulife.com의 강의를 자동으로 재생합니다. 🎉

🚀 사용법
1️⃣ 설치
필요한 패키지를 설치합니다.

bash
Copy code
pip install selenium
pip install beautifulsoup4
pip install pyautogui
2️⃣ 크롬 드라이버 설치
ChromeDriver를 설치한 후, 경로를 스크립트에 지정해야 합니다. 🌐

3️⃣ 코드 수정
lecture_codes 리스트에 자신이 듣고 싶은 과목의 코드를 입력합니다. 🎵

python
Copy code
lecture_codes = ['C00020', 'C00039', 'C00022']  # 예시
4️⃣ 스크립트 실행
스크립트를 실행한 후, 로그인을 완료하면 자동으로 강의를 재생합니다. 📚

bash
Copy code
python SDLectureAutoViewer.py
📚 코드 구조
setup_webdriver(): 웹 드라이버 설정을 초기화합니다. 🛠
fetch_lecture_durations(): 주어진 과목 코드로 강의의 길이 정보를 수집합니다. 🕵️‍♀️
play_lectures(): 주어진 과목 코드와 강의 길이 정보로 강의를 재생합니다. 🎬
⚠️ 주의사항
이 스크립트는 자동화된 방식으로 강의를 재생합니다. 사용에 따른 책임은 사용자에게 있습니다. 🚨
