# 인터넷으로 파일 다운로드 받기
# get(url)
#   - 텍스트면 text
#   - 이미지면 context

# 네이버 text 불러오기
"""
import requests
# 모듈 없다면 pip install requests (가상환경 확인 필수!)
from threading import Thread
import time

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text),resp.text)

t1 = Thread(target=getHtml, args=('http://naver.com',))
t1.start()
"""

# 이미지 불러오기
# https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.
# naver.net%2FMjAyMTAxMDdfMjMz%2FMDAxNjA5OTg4OTgxMjI1.WT8N1z9s9qGejegen-1rykYcpi6ime052aSsPDbmCA0g.
# zb_aX3GrOBVEu-Ee1G8x22rNkP23a2BPmvguJc5CN7og.JPEG.gmk72000%2FDSC08697.JPG&type=sc960_832
"""
import requests
from threading import Thread
import time

def getHtml(url):
    resp = requests.get(url)
    with open('./image.png','wb') as f:
        f. write(resp.content)
url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.\
net%2FMjAyMTAxMDdfMjMz%2FMDAxNjA5OTg4OTgxMjI1.WT8N1z9s9qGejegen-1rykYcpi6ime052aSsPDbmCA0g.\
zb_aX3GrOBVEu-Ee1G8x22rNkP23a2BPmvguJc5CN7og.JPEG.gmk72000%2FDSC08697.JPG&type=sc960_832'

t1 = Thread(target=getHtml, args=(url,))
t1.start()
"""

