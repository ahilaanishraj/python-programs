class function_bundle:
    def subfields():
            print("Subfilelds of AI is:")
            print("\t Machine Learning")
            print("\t Deep Learning")
            print("\t Natural Language Processing")
            print("\t Speech Processing")
            print("\t Robotics")
      
    def area():
            h = int(input("Enter height of trianggle:"))
            b = int(input("Enter breath of trianggle:"))
            area = (h*b)/2
            print("Area of Triangle:")
            print("\t height triagle: ", h)
            print("\t breadth of triangle: ", b)
            print("\t Area of triangle:", area)

    def perimeter():
        h1 = int(input("Enter height1 of trianggle:"))
        h2 = int(input("Enter height2 of trianggle:"))
        b = int(input("Enter breath of trianggle:"))
        area = h1+h2+b

        print("Perimeter of Triangle:")
        print("\t height1 triagle: ", h1)
        print("\t height2 triagle: ", h2)
        print("\t breadth of triangle: ", b)
        print("\t Perimeter of triangle:", area)
       
    def oddeven():
        n1 = int(input("Enter a number:"))
        if  n1 % 2 == 0:
            print(n1,"is even number")
        else:
            print(n1,"is odd number")
       
        

