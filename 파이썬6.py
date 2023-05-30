import requests
from bs4 import BeautifulSoup

url = "https://www.deu.ac.kr/www/academic_calendar_pop"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 학사일정 정보가 있는 테이블을 찾습니다.
table = soup.find("table", class_="tbl_normal")

# 테이블의 각 행을 순회하며 데이터를 출력합니다.
for row in table.find_all("tr"):
    columns = row.find_all("td")
    if len(columns) == 3:  # 데이터가 있는 행인 경우
        date = columns[0].get_text(strip=True)
        event = columns[1].get_text(strip=True)
        note = columns[2].get_text(strip=True)

        print(f"일자: {date}")
        print(f"일정: {event}")
        print(f"비고: {note}")
        print()
