# 주소록 관리 프로그램
# 파일을 매번 입력하기 귀찮아서 사용하는 configuration 방법
#0108 수정 해야함. 수정 빼고 다 함.
import sys
import time



def load_config():
    config = {}
    with open('config.ini','rt') as f:
        entries = f.readlines()
        for l in entries:
            key, values = l.split('=')
            config[key.strip()] = values.strip() #strip()->좌우 공백 제거
    return config

def load(fpath,encoding):
    with open(fpath,'rt',encoding=encoding) as f:
        return f.readlines()

def make_book(file):
    book = {}
    for line in file[1:]:
        name, phone, email, address = line.split(',')
        address = address.strip()
        book[name] = [phone, email, address]
    return book


def select_menu():
    print('1. 목록', '2. 상세보기','3. 추가', '4. 수정', '5. 삭제','6. 종료',sep='\n')
    menu = int(input('입력:'))
    return menu

# 주소록 목록 출력 + 이름 정렬
def print_list(book):
    names = list(book.keys())
    names.sort()
    print("="*50)
    print('주소록')
    print("="*50)
    for name in names:
        info = book[name]
        print(f'{name}:{info[0]},{info[1]},{info[2]}')

    print("-"*50)
    time.sleep(2)

# 세부사항
def print_detail(who):
    name = input('name :') #검색
    if name not in who:
        print(f"{name}은 목록에 없는 이름입니다.")
    else:
        info = who[name] # get, in 사용
        print(f'{name}:{info[0]},{info[1]},{info[2]}')
        time.sleep(2)

# 추가 # 현재 이름이 key 이므로 중복 확인 해줘야 함.
def add_entry(entry):
    new_entry={}
    name = input('name : ')
    if name in entry:
        print(f'{name}은 이미 존재합니다.')
        return
    phone = input('phone number:')
    email = input('email number:')
    address = input('address:')
    new_entry[name] = [phone, email, address]
    entry.update(new_entry)


# 수정 



# 삭제
def delete_entry(book):
    name = input('name :') #검색
    if name not in book:
        print(f"{name}은 목록에 없는 이름입니다.")
        time.sleep(2)
        return # 함수 종료
    
    # 진짜 삭제할꺼냐고 묻기
    answer = input('진짜 삭제하시겠습니까? [Y/N]')
    if answer == 'n'or answer =='N':
        print('메뉴로 돌아갑니다.')
        time.sleep(2)   
    elif answer == 'Y'or answer =='y':
        del(book[name])
        print(f'{name}님의 정보가 정상적으로 삭제되었습니다.')
        time.sleep(2)
    else:
        print(f'{answer}는 알맞지 않은 형식입니다.')
        time.sleep(2)
    
   
def main():
    try:
        config = load_config()
        lines = load(config['FNAME'], config['ENCODING'])
        book = make_book(lines)
        while True:
            menu = select_menu()
            if menu == 1: #목록
                print_list(book)
            elif menu == 2: #상세보기
                print_detail(book)
            elif menu == 3: #추가
                add_entry(book)
            elif menu == 4: #수정
                pass
            elif menu == 5: #삭제
                delete_entry(book)
            elif menu == 6: #종료
                sys.exit(0)
            else:
                print('Wrong number')
                

        # for n in len(book.keys()):
        #     print(book)
        #print(book,sep='\n')
    except Exception as e:
        print('예외 발생',e)
main()


