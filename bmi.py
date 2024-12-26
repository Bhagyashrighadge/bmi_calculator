# BMI Calculator with Height in Feet

def calculate_bmi(weight, height_in_meters):
    bmi = weight / (height_in_meters ** 2)
    return bmi


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("Welcome to the BMI Calculator!")

    # Prompt user for weight in kilograms
    weight = float(input("Enter your weight in kilograms: "))

    # Prompt user for height in feet
    height_feet = float(input("Enter your height in feet: "))

    # Convert height in feet to meters (1 foot = 0.3048 meters)
    height_meters = height_feet * 0.3048

    # Calculate BMI
    bmi = calculate_bmi(weight, height_meters)

    # Classify BMI
    category = classify_bmi(bmi)

    # Display the result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
