import sys
import time


class Configuration:
    def __init__(self):
    #csv 파일 경로명, encoding --> 매개변수 입력 받는 것이 아니라 설정 파일 정보를 가져옴
        config = self.load()
        self.fname = config['FNAME']
        self.encoding = config['ENCODING']
    
    def load(self):
        config={}
        with open('config.ini','rt') as f:
            entries = f.readlines()
            for l in entries:
                key, value = l.split('=')
                config[key.strip()] = value.strip()
        return config
        
    def __str__(self):
        return f'<Configuration fname:{self.fname}, encoding:{self.encoding}>'


class MenuItem:
    def __init__(self,title,func):
        self.title = title
        self.func = func

    def __str__(self):
        return f'<MenuItem {self.title}>'
    def __repr__(self):
        return f'<MenuItem {self.title} >'


#MenuItem을 관리하는 객체
class Menu:
    def __init__(self):
        self.menu_items = []

    def add(self, title, func):
        menu_item = MenuItem(title,func)
        self.menu_items.append(menu_item)

    def select_menu(self):
        for ix, menu_item in enumerate (self.menu_items,1):
            print(f'{ix}) {menu_item.title}',sep='\n')
        print()
        menu = int(float(input('번호를 입력해주세요 : ')))
        return menu

    def run_menu(self, menu):
        if 1 <= menu <len(self.menu_items)+1: #리스트 검색 써도 되는지?
            menu_item = self.menu_items[menu-1]
            menu_item.func()
        else:
            print('메뉴 번호를 다시 한 번 확인해 주세요.')


class Application:
    def __init__(self):
        self.config = Configuration()
        self.menu = Menu()
        self.create_menu(self.menu) 

    def create_menu(self, menu):
        pass

    def run(self):
        while True:
            menu = self.menu.select_menu()
            self.menu.run_menu(menu)
    
    # exit 하기 직전에 할 것. (우선 형태만)
    def destroyed(self):
        pass

    def exit(self):
        answer = input('종료하시겠습니까? [Y/N]')
        if answer == 'n'or answer =='N':
            print('메뉴로 돌아갑니다.')
            time.sleep(1)   
        elif answer == 'Y'or answer =='y':        
            self.destroyed()
            sys.exit(0)
