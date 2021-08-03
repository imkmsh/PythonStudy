1. 멀티 스레드에서 공유 자원 접근 문제를 python은 어떻게 해결하는가
- 생산자, 소비자 문제
- 모니터

2. 싱글 스레드에서 비동기 작업은 python은 어떻게 처리하는가
- coroutine, futures, async, await

# 프로세스와 스레드

![그림](https://user-images.githubusercontent.com/57826388/82154517-7c44cc80-98a9-11ea-9848-63a04a8a8b66.png)

## 1. 프로세스
- 운영체제로부터 자원을 할당받는 작업의 단위
- 디스크로부터 메모리에 적재되어 운영체제로부터 주소 공간, 파일, 메모리 등을 할당받으며 이것들을 총칭하여 프로세스라고 함
- 함수의 매개변수, 복귀 주소, 로컬 변수와 같은 임시 자료를 저장하는 프로세스 "스택"과 전역 변수들을 저장하는 데이터 섹션, 프로세스 실행 중에 동적으로 할당되는 메모리인 "힙"을 포함
## 2. 스레드
- 프로세스가 할당받은 자원을 이용하는 실행의 단위
- 한 프로세스 내에서 동작되는 여러 실행 흐름으로 프로세스 내의 Heap, Data, Code 영역을 공유
- 하나의 프로세스를 다수의 실행 단위인 스레드로 구분하여, 자원을 공유하고 자원의 생성과 관리의 중복성을 최소화하여 수행 능력을 향상시키는 것을 멀티스레딩이라고 함.
- 이 경우 각각의 스레드는 독립적인 작업을 수행해야 하기 때문에 각자의 스택과 PC 레지스터 값을 가지고 있음


# 싱글 스레드와 멀티 스레드

![싱글 스레드 & 멀티 스레드](https://media.vlpt.us/images/eunjin/post/c63d6950-7ae7-439a-9ee8-d6f145d6808a/Screen%20Shot%202021-01-17%20at%204.18.53%20PM.png)

## 1. 싱글 스레드
- 하나의 프로세스에서 하나의 스레드 실행
- 하나의 레지스터와 스택으로 표현

### 장점
  - 자원 접근에 대한 동기화를 신경쓰지 않아도 된다. 여러개의 스레드가 공유된 자원을 사용할 경우, 각 스레드가 원하는 결과를 얻게 하려면 공용 자원에 대한 접근이 통제되어야 하며, 이 작업은 프로그래머에게 많은 노력을 요구하고 많은 비용을 발생시킨다. 단일 스레드 모델에서는 이러한 작업이 필요하지 않다.
  - 작업전환 작업을 요구하지 않는다.
작업전환은 여러 개의 프로세스가 하나의 프로세서를 공유할 때 발생하는 작업으로 많은 비용을 필요로 한다.
    
### 단점
- 여러 개의 CPU를 활용하지 못한다.
프로세서를 최대한 활용하게 하려면 cluster 모듈을 사용하거나, 외부에서 여러 개의 프로그램 인스턴스를 실행시키는 방법을 사용해야 한다.

- 두 개의 작업을 하나의 스레드로 처리하는 경우와, 두 개의 스레드로 처리하는 경우를 가정했을 때, 후자의 경우는 짧은 시간 동안 2개의 스레드가 번갈아가면서 작업을 수행한다. 그래서 동시에 두 작업이 처리되는 것과 같이 느끼게 된다.

- 오히려 두 개의 스레드로 작업한 시간이 싱글스레드로 작업한 시간보다 더 걸릴 수도 있는데, 그 이유는 스레드 간의 작업전환(context switching)에 시간이 걸리기 때문이다.

- 따라서 단순히 CPU만을 사용하는 계산작업이라면, 오히려 멀티스레드보다 싱글스레드로 프로그래밍하는 것이 더 효율적이다.
  
~~~
from threading import Thread

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    return

if __name__ == "__main__":
    START, END = 0, 100000000
    result = list()
    th1 = Thread(target=work, args=(1, START, END, result))
    
    th1.start()
    th1.join()

print(f"Result: {sum(result)}")
~~~

## 2. 멀티 스레드
- 프로그램을 다수의 실행 단위로 나누어 실행.
- 프로세스 내에서 자원을 공유하여 자원 생성과 관리의 중복을 최소화
- 서버가 많은 요청을 효율적으로 수행할 수 있는 환경을 제공
- 각각의 스레드가 고유의 레지스터와 스택으로 표현됨.

### 장점
- 새로운 프로세스를 생성하는 것보다 기존 프로세스에서 스레드를 생성하는 것이 빠르다.
- 프로세스의 자원과 상태를 공유하여 효율적으로 운영이 가능하다.
- 프로세스의 작업전환보다 스레드의 작업전환이 더 빠르다.

### 단점
- 하나의 스레드만 실행중일 때는 실행시간이 오히려 지연될 수 있다.
- 멀티 스레딩을 위해 운영체제의 지원이 필요하다.
- 스레드 스케쥴링을 신경써야 한다.

~~~
from threading import Thread

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    return

if __name__ == "__main__":
    START, END = 0, 100000000
    result = list()
    th1 = Thread(target=work, args=(1, START, END//2, result))
    th2 = Thread(target=work, args=(2, END//2, END, result))
    
    th1.start()
    th2.start()
    th1.join()
    th2.join()
~~~

# 멀티 프로세스
~~~
from multiprocessing import Process, Queue

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return

if __name__ == "__main__":
    START, END = 0, 100000000
    result = Queue()
    th1 = Process(target=work, args=(1, START, END//2, result))
    th2 = Process(target=work, args=(2, END//2, END, result))
    
    th1.start()
    th2.start()
    th1.join()
    th2.join()

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp
    print(f"Result: {total}")
~~~

# 싱글 스레드 + 코루틴

~~~
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())
~~~

~~~
def min():
    current = yield
    while True:
        value = yield current
        current = min(value, current)
        
it = min()
next(it)
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-6))
~~~

# 동기화 문제
동기화 문제는 상호 배제 문제


## 임계 영역(critical section)을 lock으로 보호

- lock은 동기화의 가장 근본 수단
- 공유 변수 lock, 0 또는 1의 값으로 확인


## locking을 원자적으로 처리하는 하드웨어 명령어 

- 공유 변수라는 문제를 해결하기 위해 운영체제가 값 확인과 진입을 원자적으로 처리
- non-preemptive command

### `TestAndSet()`
- 한 워드의 내용을 확인하고 수정하는 연산을 원자적으로 처리

~~~
boolean TestAndSet(boolean *target) {
    boolean rv = *target
    *target = TRUE
    return rv
}
  
do {
    while (TestAndSet(&lock)) // do nothing
        // critical section
    lock = FALSE
        // remainder section
}
while (TRUE)
~~~

- 누가 먼저 lock을 푸냐의 문제를 해결하기 위해 한정된 대기(bounded wait)를 보장, 공유 데이터 `boolean lock`으로
~~~
do {
    waiting[i] = TRUE
    key = TRUE
    while (waiting[i] && key)
        key = TestAndSet(&lock)
    waiting[i] = FALSE
        // critical section

    j = (i + 1) % n
    while ((j != i) && !waiting[j])
        j = (j + 1) % n
       
    if (j == i)
        lock = FALSE
    else
        waiting[j] = FALSE
        // remainder section
}
while (TRUE)
~~~
       
###`Swap()`
- 두 워드의 내용을 서로 교환하는 연산을 원자적으로 처리
~~~
void Swap(boolean *a, boolean *b) {
    boolean temp = *a
    *a = *b
    *b = temp
}
  
do {
    key = TRUE
    while (key == TRUE)
        Swap(&lock, &key)
        // critical section
    lock = FALSE
        // remainder section
}
while (TRUE)
~~~

## Semaphore
  

    

도움: https://www.youtube.com/watch?v=_yqQLDujlg8
