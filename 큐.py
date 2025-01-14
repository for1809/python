'''
문제
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''
'''
from sys import stdin as s
n = int(s.readline())
lst1 = []
for i in range(n):
    prompt = s.readline().strip().split()
    if prompt[0] == 'push':
        lst1.append(prompt[-1])
    elif prompt[0] == 'pop':
        if lst1:
            print(lst1.pop(0))
        else:
            print(-1)
    elif prompt[0] == 'size':
        print(len(lst1))
    elif prompt[0] == 'empty':
        print(0) if lst1 else print(1)
    elif prompt[0] == 'front':
        print(lst1[0]) if lst1 else print(-1)
    elif prompt[0] == 'back':
        print(lst1[-1]) if lst1 else print(-1)
'''
# 개선안
# deque 사용 list와 유사하나 양방향으로 pop, append 가능. popleft, appendleft
from collections import deque
from sys import stdin as s

n = int(s.readline())
que = deque()
for i in range(n):
    prompt = s.readline().strip().split()
    if prompt[0] == 'push':
        que.append(prompt[-1])
    elif prompt[0] == 'pop':
        print(que.popleft()) if que else print(-1)
    elif prompt[0] == 'size':
        print(len(que))
    elif prompt[0] == 'empty':
        print(0) if que else print(1)
    elif prompt[0] == 'front':
        print(que[0]) if que else print(-1)
    elif prompt[0] == 'back':
        print(que[-1]) if que else print(-1)