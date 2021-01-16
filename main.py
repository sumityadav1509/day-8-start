def paint_area(height,width,per_can_area):
  number_of_cans=(int(height)*int(width))/int(per_can_area) 
  print(round(number_of_cans))


paint_area(input("Height: "), input("Width: ") , input("Per Can: "))

