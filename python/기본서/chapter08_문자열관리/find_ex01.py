# 프로토콜이 무엇인지, 파일명은 무엇인지 출력하시오.
# 프로토콜 : https
# 파일명 : seoul.html

url = "https://www.naver.com/blog/travel/seoul.html"

if url.find(':') != -1:
    print("Protocol :", url[:url.find(":")])

if url.rfind('/') != -1:
    print("file name :", url[url.rfind("/")+1::])

if url.rfind('.') != -1:
    print("file type :", url[url.rfind(".")+1::])
