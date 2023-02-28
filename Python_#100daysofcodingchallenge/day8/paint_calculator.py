import math
   
def paint_cal(height, width, cover):
    total = math.ceil((height * width) / cover)
    print(f"You'll need {total} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall:  "))
coverage = 5

paint_cal(height=test_h, width=test_w, cover=coverage)