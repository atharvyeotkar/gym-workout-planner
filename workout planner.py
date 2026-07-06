

workout = {"monday":"""🏋️ push day \nIncline DB Press – 3 sets,
Flat Bench – 3 sets
Shoulder Press – 3 sets
Lateral Raises – 4 sets
Tricep Pushdown – 3 sets
Overhead Tricep Extension – 3 sets""",

           "tuesday":"""💪 pull day \nPull-ups – 3 sets
Barbell Rows – 3 sets
Cable Rows – 3 sets
Face Pulls – 3 sets
Bicep Curl – 3 sets
Hammer Curl – 3 sets""",

           "wednesday":"""🦵 leg day \nSquat – 3 sets
RDL – 3 sets
Leg Press – 3 sets
Calf Raises – 4 sets
Leg Curl – 3 sets""",

           "thursday":"""🔥 upper asthetic day \nIncline Press
Pull-ups
Lateral Raises
Chest Fly
Biceps
Triceps""",

           "friday":"💥 arms,neck,abs",

           "saturday":"🏃 cardio",

           "sunday":"😴 rest"}


while True:
 print("========== Gym Workout Planner ===========")
 print("1. Today's Workout")
 print("2. Full Week Plan")
 print("3. Bmi Calculator")
 print("4. exit")
 
 choice = (input("Enter your choice:"))



 if choice == "1":

    day = input("enter day of week:").strip().lower()

    print(workout.get(day,"❌Invalid day"))
    input("\nPress Enter to Return....")
 elif choice == "2":
    for key, value in workout.items():
        print("\n-----------------")
        print(key.title())
        print("-----------------")
        print(value)
    input("\nPress Enter to Return....")

 elif choice == "3":
    weight =float(input("Enter Your Weight (kg):"))
    height =float(input("Enter your Height (meters):"))

    bmi = weight / height ** 2

    print(f"Your  BMI is :{bmi :.2f}")
    input("\nPress Enter to Return....")
 elif choice == "4":
    print("👋 Goodbye!!!!")
    break

 else:
    print("❌ Invalid Choice")
    input("\nPress Enter to Return....")









