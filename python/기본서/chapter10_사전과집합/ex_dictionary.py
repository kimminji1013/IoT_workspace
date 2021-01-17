# alphbet counting / word counting
song = """by the rivers of babylon, there we 
sat down yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

"""
alphabet = dict()
for letter in song:
    if letter.isalpha() == False: #alphabet 아니라면 0(False) 반환
        continue

    letter = letter.lower()
    if letter not in alphabet:
        alphabet[letter] = 1
    else:
        alphabet[letter] += 1

print(alphabet)
"""

# 단어 단위로
"""
word_dic = dict()
song_line = song.splitlines()

for line in song_line:
    for word in line.split():
        word = word.lower()
        if word not in word_dic:
            word_dic[word] = 1
        else:
            word_dic[word] += 1

# 단어 순서로 출력
key_list = list(word_dic.keys())
key_list.sort()
for word2 in key_list:
    print(word2, word_dic[word2])
    #num = word_dic[word2]
    #print(word2, num)
"""

# 알파벳 빈도수로 출력
#"""
alphabet = dict()
for letter in song:
    if letter.isalpha() == False: #alphabet 아니라면 0(False) 반환
        continue

    letter = letter.lower()
    if letter not in alphabet:
        alphabet[letter] = 1
    else:
        alphabet[letter] += 1

def get_value(a):
    return a[1]

items = list(alphabet.items())
items.sort(reverse=True, key=get_value)
# item을 내림차순으로 정렬할 것인데, 정렬key를(사전key아님)
# value값[a1]으로 정렬하겠다.
for k,v in items:
    print(f'{k} : {v}')
#"""

# 함수를 코드 중간에 한 번 사용 위해 만드는 것이 번거로울 때
# 람다 함수를 이용
"""def get_value(a):
    return a[1]"""
"""
func = lambda a:a[1]
items = ('a',10)
print(func(items))
"""