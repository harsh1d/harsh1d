# # class Rectangle:

# #     def __init__(self,length,width):
# #         self.length = length
# #         self.width = width
        
# #         def area(self):
# #             return (self.length * self.width)
        
# #     rectangle1 = Rectangle (12,11)
# #     rectangle2 = Rectangle (12,10)

    
# #     print("Area of the first rectangle is",rectangle1.area())  # Area of the first rectangle is 132
# #     print("Area of the secdond rectangle is",rectangle2.area())

# # class Rectangle:

# #     def __init__(self,length,width):
# #         self.length = length
# #         self.width = width

# #     def area(self):
# #         return (self.length * self.width)

# # # creating objects for class
# # rectangle1 = Rectangle(12,11)
# # rectangle2 = Rectangle(12,10)
# # rectangle3 = Rectangle(10,12)

# # # printing the area of the rectangles
# # print("Area of the first rectangle is",rectangle1.area()) # Area of the first rectangle is 132
# # print("Area of the second rectangle is",rectangle2.area()) # Area of the second rectangle is 120
# # print("Area of the third rectangle is",rectangle3.area())   # Area of the third rectangle is 120

# class Rectangle:

#   def _init_(self, length, width):
#     self.length = length
#     self.width = width

#   def area(self):
#     return self.length * self.width


# # Create three different Rectangle objects
# rectangle1 = Rectangle(10, 5)
# rectangle2 = Rectangle(6, 3)
# rectangle3 = Rectangle(8, 4)


# # Function to display the area of a rectangle
# def display_area(rectangle):
#   print(f"The area of the rectangle is: {rectangle.area()}")


# # Display the area of all three rectangles
# display_area(rectangle1)
# display_area(rectangle2)
# display_area(rectangle3)

class Rectangle:

  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width


# Create three different Rectangle objects
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(6, 3)
rectangle3 = Rectangle(8, 4)
print(f"The area of the rectangle is: {rectangle1.area()}")
print(f"The area of the rectangle is: {rectangle2.area()}")
print(f"The area of the rectangle is: {rectangle3.area()}")
