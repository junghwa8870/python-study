
'''
# 순위
# 가수명
# 앨범명
# 노래 제목

멜론일간차트순위_2024년_5월_31일_11시기준.txt
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs
from bs4 import BeautifulSoup
# 뷰티풀수프 임포트


d = datetime.today()

file_path = f'C:/myworkspace/upload/멜론일간차트순위_{d.year}년_{d.month}월_{d.day}일_{d.hour}시 기준.txt'

# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해 주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options=option, service=service)

with codecs.open(file_path, mode='w', encoding='utf-8') as f:
    
    #페이지 이동
    driver.get('https://www.melon.com/chart/index.htm')

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for cnt in [50, 100]:
        
        # 곡 정보가 있는 tr 리스트를 지목해서 얻어오자 (Lst50, Lst100으로 나누어져 있음.)
        song_tr_list = soup.select(f'.lst{cnt}')

        for song_tr in song_tr_list:
            
            # 순위 찾기
            rank = song_tr.select_one('div.wrap.t_center').text.strip()
            print(rank)

            # 가수 이름 찾기
            artist_name = song_tr.select_one('div.wrap div.ellipsis.rank02 > a').text.strip()
            print(artist_name)

            # 앨범명 찾기
            album_name = song_tr.select_one('div.wrap div.ellipsis.rank03 > a').text.strip()
            print(album_name)

            # 노래명 찾기
            song_name = song_tr.select_one('div.wrap div.ellipsis.rank01 > span > a').text.strip()
            print(song_name)

            print('=' * 40)

            f.write(f'# 순위: {rank}\n')
            f.write(f'# 가수명: {artist_name}\n')
            f.write(f'# 앨범명: {album_name}\n')
            f.write(f'# 노래 제목: {song_name}\n')
            f.write('-' * 40 + '\n')

driver.close()            




'''
# 멜론 차트 페이지 URL
url = 'https://www.melon.com/chart/index.htm'

# 실제 브라우저 요청을 모방하는 HTTP 헤더
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
}

# 멜론 차트 페이지에 GET 요청 보내기
response = requests.get(url, headers=headers)

# 요청이 성공했는지 확인
if response.status_code == 200:
    print("페이지를 성공적으로 가져왔습니다.")  # 디버깅용 출력

    # BeautifulSoup을 사용하여 HTML 콘텐츠 파싱
    soup = BeautifulSoup(response.content, 'html.parser')
    print("HTML 파싱을 완료했습니다.")  # 디버깅용 출력

    # 차트 테이블 찾기
    chart_list = soup.select('tr[data-song-no]')
    print(f"차트에서 {len(chart_list)}개의 항목을 찾았습니다.")  # 디버깅용 출력

    # 파일을 열어 데이터 쓰기
    with open(file_path, 'w', encoding='utf-8') as file:
        # 헤더 쓰기
        header = f"{'순위':<10}{'가수명':<20}{'앨범명':<30}{'노래 제목':<30}\n"
        file.write(header)
        print(header.strip())  # 디버깅용 출력

        # 추출한 데이터를 반복하여 각 행을 파일에 쓰기
        for chart in chart_list:
            rank = chart.select_one('span.rank').text.strip()
            title = chart.select_one('div.ellipsis.rank01 a').text.strip()
            artist = chart.select_one('div.ellipsis.rank02 a').text.strip()
            album = chart.select_one('div.ellipsis.rank03 a').text.strip()
            line = f"{rank:<10}{artist:<20}{album:<30}{title:<30}\n"
            file.write(line)
            print(line.strip())  # 디버깅용 출력

else:
    print(f"페이지를 가져오지 못했습니다. 상태 코드: {response.status_code}")
'''