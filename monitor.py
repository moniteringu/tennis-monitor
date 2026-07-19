import requests
from bs4 import BeautifulSoup

URL = "https://www.ksponco.or.kr/spm/reservationStatus/tennis/waitList.do?textSize=normal"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers, timeout=20)
response.raise_for_status()

print("접속 성공!")
print("상태코드:", response.status_code)

soup = BeautifulSoup(response.text, "lxml")

print("페이지 제목:")
print(soup.title.text if soup.title else "제목 없음")
