from threading import Lock

class Bridge:
    def __init__(self):
        self.counter = 0
        self.name = '아무개'
        self.addres = '몰라'
        self.lock = Lock()

    def across(self, name, address):
        self.lock.acquire()
        # Critical Section (임계영역)----┐
        self.counter += 1 
        self.name = name
        self.address = address
        self.check()
        # Critical Section (임계영역)----┘
        self.lock.release()

    def toString(self):
        return "이름: {}, 출신:{}, 도전횟수: {}"\
            .format(self.name, self.address, self.counter)
       
   
    def check(self):
       # self.lock.acquire()
        if self.name[0] != self.address[0]:
            print("문제 발생 !!!" + self.toString())
       # self.lock.release()