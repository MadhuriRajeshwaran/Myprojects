class assignment2():
    def BMI():
    print("BMI Calculator")
    Height=float(input("Enter your height in meters:"))
    Weight=float(input("Enter your weight in kilogram:"))
    X=Height*Height
    Bmi=(Weight/X)
    if(Bmi<=18.5):
        print("You are underweight")
    elif(Bmi<=25):
        print("You are Normal")
    elif (Bmi<=30):
        print ("You are Over weight")
    else:
        print("Your are Obese")
        return Bmi
    
    def OddEven():
        x=int (input("Enter a number:"))
        if(x%2==1):
            print(x,"is odd")
            Value="Odd"
        else: 
            print(x,"is even")
            Value="Even"
        return Value     
    
    def Elegible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Gender=='Male' and Age>=21):
            print("Eligible")
        elif(Gender=='Male' and Age<21):
            print("Not Eligible")
        elif(Gender=='Female' and Age>=18):
            print("Eligible")
        else:
            print("Not Eligible")  
            return Age
        
    def triangle():
        H1= int(input("Height:"))
        B1=int(input("Breadth:"))
        Area=(H1*B1)/2
        print("Area of Triangle:",Area)
        X1=int(input("Height1:"))
        X2=int(input("Height2:"))
        X3=int(input("Breadth:"))
        Perimeter=X1+X2+X3
        print("Perimeter of Triangle:",Perimeter)
        return Area     
    
    def percentage(a,b,c,d,e):
        Total=a+b+c+d+e
        percentage=Total/5
        print("Subject1=",a)
        print("subject2=",b)
        print("subject3=",c)
        print("subject4=",d)
        print("subject5=",e)
        print("Total:",Total)
        print("Percentage:",percentage)
        return percentage   
    