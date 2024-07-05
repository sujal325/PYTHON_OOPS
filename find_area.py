class Shape:

    def __init__(self):
        print(
            """
                //TYPE 1 FOR SQUARE//
                //TYPE 2 FOR RECTANGLE//
                //TYPE 3 FOR TRIANGLE//
                //TYPE 4 FOR CIRCLE//
            """
        )
        self.key()

    def key(self):
        key = int(input("WHICH SHAPE AREA DO YOU WANT TO FIND: "))
        if key == 1:
            self.square()
        elif key == 2:
            self.rectangle()
        elif key == 3:
            self.triangle()
        elif key == 4:
            self.circle()
        else:
            print("Invalid input. Please select a number between 1 and 4.")

    def square(self):
        side = int(input("Enter the length of the side of the square: "))
        area = side * side
        print(f"Area of the square is {area} square units.")

    def rectangle(self):
        length = int(input("Enter the length of the rectangle: "))
        breadth = int(input("Enter the breadth of the rectangle: "))
        area = length * breadth
        print(f"Area of the rectangle is {area} square units.")

    def triangle(self):
        base = int(input("Enter the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        area = 0.5 * base * height  # Formula for the area of a triangle
        print(f"Area of the triangle is {area} square units.")

    def circle(self):
        radius = int(input("Enter the radius of the circle: "))
        area = 3.14 * radius * radius  # Using pi as 3.14 for simplicity
        print(f"Area of the circle is {area} square units.")


s = Shape()
