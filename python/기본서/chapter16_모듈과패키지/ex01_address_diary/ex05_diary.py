# 모델 객체 : 정보(데이타)만을 저장하는 Class 
import time
import sys
from app_base import Application


class DiaryApp(Application):
    def __init__(self):
        super().__init__()

    def create_menu(self, menu):
        menu.add('쓰기',self.write)
        menu.add('수정',self.update)
        menu.add('삭제',self.delete)
        menu.add('종료',self.exit)
        

    def write(self):
        print('오늘의 일기')

    def update(self):
        print('이전 일기 수정')

    def delete(self):
        print('일기 삭제')

def main():
    app = DiaryApp()
    app.run()

main()