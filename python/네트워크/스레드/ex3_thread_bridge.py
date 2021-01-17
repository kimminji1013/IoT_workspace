from bridge import Bridge
from knight import Knight

print("시뮬레이션을 시작합니다.")
bridge = Bridge()  # 공유 자원이라서 업데이트할 때 공유자원 변수가 섞여 문제가 생김-> lock 사용
                    # acqure(), release()

Knight(bridge, '김민지', '김김').start()
Knight(bridge, '박지인', '박박').start()
Knight(bridge, '임가현', '임임').start()
Knight(bridge, '오영은', '오오').start()

