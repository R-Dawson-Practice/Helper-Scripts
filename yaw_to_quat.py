import math

def yaw_to_quat(yaw):
    x = 0
    y = 0
    z = math.sin(yaw/2)
    scalar = math.cos(yaw/2)
    return (x,y,z,scalar)

def main():
    yaw = 1.57
    quat = yaw_to_quat(yaw)
    print(quat)

if __name__ == "__main__":
    main()