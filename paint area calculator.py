from turtle import width
import math
def paint_calc(height,width,cover):
  area=height*width
  num_of_cans=math.ceil(area/coverage)
  print(f"No. of cans required to paid the wall is {num_of_cans}")
height_h=int(input("what is the height of wall1 :"))
width_w=int(input("what is the width of the wall :"))
coverage=5
paint_calc(height=height_h,width=width_w,cover=coverage)