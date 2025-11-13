from collections import deque
from dataclasses import dataclass
@dataclass
class imu_sample:
    num1:int
    string1:str
    bool1:bool

def main():
    log = deque()
    target = None
    for i in range(10):
        s = imu_sample(num1=i, string1=f"Hello {i}", bool1=True)
        log.append(s)

    candidate = None
    for i in log:
        if i.string1 == "Hello5":
            candidate = i
    if candidate:
        print(candidate)

if __name__ in "__main__":
    main()