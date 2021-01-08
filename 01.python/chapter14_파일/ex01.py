# data.csv 파일 이용
def load(file_path):
    with open(file_path,'rt',encoding='UTF-8') as f:
        return f.readlines()

def convert(lines):
    data = {}
    for line in lines[1:]:
        items = line.split(',')
        name = items[0]
        scores = items[1:]
        data[name] = list(map(int,scores)) 
        # 사전에 추가하는 내용
        # map함수로 value 값 int로 만들어주기
        # int가 되면 문자열 마지막에 있던 \n 사라짐. 
    return data

def main():
    try:
        #lines = load('data.csv')
        file_path = input('file name:')
        lines = load(file_path)
        data = convert(lines)
        print(data, sep='\n')
    except Exception as e:
        print('예외 발생',e)
    
main()
