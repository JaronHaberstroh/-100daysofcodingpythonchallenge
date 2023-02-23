# Create a BMI calculator with user input for height/weight

# Get user input for height/weight

height = float(input("Enter your height in m: "))

weight = float(input("Enter your weight in kg: "))

# Calculate user BMI (weight / height ** 2)

bmi = round(weight / height ** 2)

# Create if/else condition to tell user if they are: 

if bmi > 35:
    print(f"Your BMI is {bmi} and you considered clinically obese.")
elif bmi >= 30:
    print(f"Your BMI is {bmi} and you are considered obese.")
elif bmi > 25:
    print(f"Your BMI is {bmi} and you are overweight.")
elif bmi > 18.5:
    print(f"Your BMI is {bmi} and you are normal weight.")
else:
    print(f"Your BMI is {bmi} and your consider underweight.")
    
# underweight, normal weight, overweight, obese, clinically obese