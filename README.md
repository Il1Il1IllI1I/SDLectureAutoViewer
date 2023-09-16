# 🎓 **SDLectureAutoViewer**

---

## 📌 **목차**

1. [📜 설명](#-설명)
2. [🎨 주요 기능](#-주요-기능)
3. [🛠️ 사용된 기술](#-사용된-기술)
4. [🚀 사용법](#-사용법)
5. [📚 코드 구조](#-코드-구조)
6. [⚠️ 주의사항](#-주의사항)

---

## 📜 **설명**

Selenium과 BeautifulSoup를 사용하여 `www.sdulife.com`의 강의를 자동으로 시청하세요. 🎉

---

## 🎨 **주요 기능**

- 📝 **과목별 강의 정보 수집**: 각 과목의 강의 정보를 자동으로 수집합니다.
- 🎥 **강의 자동 재생**: 수집된 정보를 바탕으로 강의를 자동으로 재생합니다.

---

## 🛠️ **사용된 기술**

- 🐍 **Python**: 사용된 프로그래밍 언어입니다.
- 🌐 **Selenium**: 웹 브라우저를 자동으로 제어할 수 있는 라이브러리입니다.
- 🍲 **BeautifulSoup**: 웹 페이지 내용을 분석할 수 있는 라이브러리입니다.

---

## 🚀 **사용법**

### 1️⃣ 설치
필요한 패키지를 설치합니다.

```bash
pip install selenium
pip install beautifulsoup4
pip install pyautogui
```

### 2️⃣ 크롬 드라이버 설치
[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)를 설치한 후, 경로를 스크립트에 지정해야 합니다. 🌐

### 3️⃣ 코드 수정
`lecture_codes` 리스트에 자신이 듣고 싶은 과목의 코드를 입력합니다. 🎵

```python
lecture_codes = ['C00020', 'C00039', 'C00022']  # 예시
```

### 4️⃣ 스크립트 실행
스크립트를 실행한 후, 로그인을 완료하면 자동으로 강의를 재생합니다. 📚

```bash
python SDLectureAutoViewer.py
```

---

## 📚 코드 구조

- `setup_webdriver()`: 웹 드라이버 설정을 초기화합니다. 🛠
- `fetch_lecture_durations()`: 주어진 과목 코드로 강의의 길이 정보를 수집합니다. 🕵️‍♀️
- `play_lectures()`: 주어진 과목 코드와 강의 길이 정보로 강의를 재생합니다. 🎬

---

## ⚠️ 주의사항

- 이 스크립트는 자동화된 방식으로 강의를 재생합니다. 사용에 따른 책임은 사용자에게 있습니다. 🚨

