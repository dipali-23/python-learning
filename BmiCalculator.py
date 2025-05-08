def bmicalculator(weight, height):
    """
    Calculate the Body Mass Index (BMI) based on weight and height.

    Parameters:
    weight (float): Weight in kilograms.
    height (float): Height in meters.

    Returns:
    float: The calculated BMI.
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    
    bmi = weight / (height ** 2)
    return round(bmi, 2)
w= float(input("Enter weight in kg: "))
u=int(input("select unit for height: 1 for cm, 2 for m,3 for inches,4 for foot: "))
if u==1:
    h= float(input("Enter height in cm: "))
    h=h/100
elif u==2:
    h= float(input("Enter height in m: "))
elif u==3:
    h= float(input("Enter height in inches: "))
    h=h*0.0254
elif u==4:
    h= float(input("Enter height in foot: "))
    h=h*0.3048
else:
    print("Invalid unit selected.")
    exit()
try:
    bmi = bmicalculator(w, h)
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
    print(f"Your BMI is: {bmi}")
except ValueError as e:
    print(e)