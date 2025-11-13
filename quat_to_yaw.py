import math


def quat_to_yaw(x, y, z, w):
    return math.atan2(2 * (w * z + x * y), 1-2*(y*y+z*z))

def rad_to_deg(rad):
    return rad * 180/math.pi

def main():
    yaw_rad = quat_to_yaw(
0, 0, 0.706825181105366, 0.7073882691671998
    )
    yaw_deg = rad_to_deg(yaw_rad)
    print(yaw_deg)
    print(yaw_rad)


if __name__ == "__main__":
    main()
