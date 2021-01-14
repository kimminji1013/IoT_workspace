# 주소록 관리 프로그램 
# 파일을 매번 입력하기 귀찮아서 사용하는 configuration 방법
#0108 수정 해야함. 수정 빼고 다 함.
import sys
import time
import traceback



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
# 수정 작업에서는 기존 내용을 먼저 보여주는 작업 먼저 수행한다.
def update_entry(book):
    new_entry={}
    name = input('name : ')
    if name not in book:
        print(f'{name}은 존재하지 않습니다.')
        return
    old_phone, old_email, old_addr = book[name]  # unpack 기능. 튜플 리스트 다 가능
    print('변경이 없는 경우 enter를 눌러주세요.')
    phone = input(f'phone number [{old_phone}]:')
    if phone.strip() == '': # 엔터를 친 경우,
        phone = old_phone
    email = input(f'email number [{old_email}]:')
    if email.strip() == '': # 엔터를 친 경우,
        email = old_email
    address = input(f'address [{old_addr}]:')
    if address.strip() == '': # 엔터를 친 경우,
        address = old_addr    
    # 사전에 추가
    new_entry[name] = [phone, email, address]
    print('정상적으로 수정되었습니다.')
    book.update(new_entry)
    time.sleep(2)


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

# 업데이트 된 내용 파일에 저장
# l = [1,2]--->','.join(l) = '1, 2' 문자열로 만들어주는 모듈
def save(book, fpath, encoding):
    with open(fpath,'wt',encoding=encoding) as f:
        f.write('이름,전화번호,email,주소\n')
        for name, value in book.items():
            scores = ','.join(value)
            line = f'{name},{scores}\n' # 개행문자도 데이타로서 넣어줘야 함
            f.write(line)


# 종료
# 종료 여부 질의, 업데이트된 주소록 저장 (사전, 저장할 파일 경로 필요) 
def exit(book, fpath, encoding):
    answer = input('종료할까요? [Y/N]')
    if answer == 'n'or answer =='N':
        print('메뉴로 돌아갑니다.')
        time.sleep(2)
        return
    
    save(book, fpath, encoding)
    sys.exit(0)
    

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
                update_entry(book)
            elif menu == 5: #삭제
                delete_entry(book)
            elif menu == 6: #종료
                #sys.exit(0) 그냥 시스템 종료
                exit(book, config['FNAME'], config['ENCODING'])
            else:
                print('Wrong number')
                

        # for n in len(book.keys()):
        #     print(book)
        #print(book,sep='\n')
    except Exception as e:
        print('예외 발생',e)
        # # 예외가 발생한 시점까지 거친 함수 목록 출력
        traceback.print_stack()
        # # 구체적인 예외 내용 출력
        traceback.print_exc()
        # traceback 부분은 개발이 끝나고 지움. 
main()


