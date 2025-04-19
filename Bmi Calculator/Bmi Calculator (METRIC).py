
# Metric BMI Calculator by Thandolwethu Zitha

def main():
    print("Metric Body Mass Index Calculator")
    menu()
    mass = weight()
    Height = height()
    Age = age()
    bmi = BMI(mass, Height)
    wclass = weight_class(bmi, Age)
    print(f"Your BMI is {bmi:.2f} which is {wclass}")
    recommendations(wclass)


def menu():
    print("A. Female")
    print("B. Male")
    choice = input("Choose your gender: ")
    return choice


def weight():
    mass = float(input("Enter your body weight in kg : "))
    return mass


def height():
    Height = float(input("Enter your height in m: "))
    return Height


def BMI(mass, Height):
    bmi = (mass / Height ** 2)
    return bmi


def age():
    print("How old are you? ")
    print("A. < 18 (Youth)")
    print("B. > 18 (Adult)")
    Age = input("Choose your age, A or B: ")
    return Age


def weight_class(bmi, Age):
    if Age == "A":
        if bmi < 16.5:
            return "Underweight"
        elif 16.5 <= bmi <= 23:
            return "Normal"
        elif 23 <= bmi <= 28:
            return "Overweight"
        else:
            return "Obese"
    else:
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi <= 25:
            return "Normal"
        elif 25 <= bmi <= 30:
            return "Overweight"
        else:
            return "Obese"


def recommendations(wclass):
    if wclass == "Overweight" or wclass == "Obese":
        rec = input("Would you like recommendations on how to shed some weight "
                    "by altering your diet and daily habits? , Yes or No (Case Sensitive) ")
        if rec == "Yes":
            print("Making an effort to find out about safe and healthy weight loss methods is already a step in the "
                  "right direction. " +
                  "Ah look at you already getting your steps in!")
        else:
            print("That's okay! When the time comes and you're to improve your health hit me up!")
    elif wclass == "Underweight":
        rec2 = input("Would you like recommendations on how to gain a few healthy kilos"
                     + " by altering your diets and daily habits? " +
                     "Yes or No (Case Sensitive)")
        if rec2 == "Yes":
            print("Making an effort to find out about safe and healthy weight gain methods is already a step in the "
                  "right direction" +
                  "Lets get started")
        else:
            print("That's okay! When the time comes and you're to improve your health hit me up!")
    elif wclass == "Normal":
        print("Your BMI is in the healthy range. Keep it up!")

    print("Recommendations Update Coming Soon...")


main()
