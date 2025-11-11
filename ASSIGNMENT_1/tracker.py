print("""
hello everyone.
here Tamanna
from section C 
date-09-11-2025
project title-daily_calorie_tracker\n""")
print("""hello everyone its a little project which tells you about your daily limit of calorific value and warn you if your daily limit crosses the limit you decided \n""")

meal=[]
calorie=[]
x=int(input("enter the number of meals in digit you eat today : "))
for i in range(x):
    meals=input("enter your meal name - ")
    calories=float(input("enter your calories respectively to the meal -  "))
    meal.append(meals)
    calorie.append(calories) 
print(f"Meal Names List: {meal}")
print(f"Calorie List:    {calorie}")
p=float(input("enter your daily calorie limit: "))
s=sum(calorie)
print("the total calories you eat today is:",s)
a=s/x
print("the average of your intake calorie is:",a)
if p>s:
    print("\n⚠️ You have exceeded your daily calorie limit!")
elif p==s:
    print("\n⚠️you are very near to cross your dail limit!")
else:
     print("\n✅ Great! You are within your daily calorie limit.")
for i in range(x):
    print(f"{meal[i]}\t\t{calorie[i]}")
print("--------------------------------")
print(f"Total:\t\t{s}")
print(f"Average:\t{a:.2f}")
save = input("\nDo you want to save this session report? (yes/no): ").strip().lower()
if save == "yes":
    from datetime import datetime
    filename = "calorie_log.txt"
    with open(filename, "w") as f:
        f.write("Daily Calorie Tracker Log\n")
        f.write(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        f.write("--------------------------------\n")
        for i in range(x):
            f.write(f"{meal[i]}\t\t{calorie[i]}\n")
        f.write("--------------------------------\n")
        f.write(f"Total:\t\t{s}\n")
        f.write(f"Average:\t{a:.2f}\n")
        if p > s:
            f.write("\n⚠️ You have exceeded your daily calorie limit!\n")
        elif p == s:
            f.write("\n⚠️ You are very near to crossing your daily limit!\n")
        else:
            f.write("\n✅ Great! You are within your daily calorie limit.\n")
    print(f"\nSession report saved successfully in 'calorie_log.txt'!")