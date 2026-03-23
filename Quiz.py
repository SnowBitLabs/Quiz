print("Welcome to Quiz 2.0 🚀")
print("Type correct answers (a, b, c, d) and see your result at the end\n")

point = 0

# Q1
print("Q1. What is the part of a bike or car on which the wheel turns?")
print("(a) ayle\n(b) axle\n(c) fulcrum\n(d) axis")
ans = input("Your answer: ").lower()
if ans == "b":
    print("Correct ✅")
    point += 1
else:
    print("Wrong ❌")

# Q2
print("\nQ2. What is the only metal that is liquid at room temperature?")
print("(a) Mercury\n(b) Gallium\n(c) Cesium\n(d) Bromine")
ans = input("Your answer: ").lower()
if ans == "a":
    print("Correct ✅")
    point += 1
else:
    print("Wrong ❌")

# Q3
print("\nQ3. Which continent has the most countries?")
print("(a) Asia\n(b) Europe\n(c) Africa\n(d) South America")
ans = input("Your answer: ").lower()
if ans == "c":
    print("Correct ✅")
    point += 1
else:
    print("Wrong ❌")

# Q4
print("\nQ4. Which gas makes up most of Earth’s atmosphere?")
print("(a) Argon\n(b) Oxygen\n(c) CO2\n(d) Nitrogen")
ans = input("Your answer: ").lower()
if ans == "d":
    print("Correct ✅")
    point += 1
else:
    print("Wrong ❌")

# Q5
print("\nQ5. What is the tallest mountain from base to peak?")
print("(a) K2\n(b) Everest\n(c) Mauna Kea\n(d) Kangchenjunga")
ans = input("Your answer: ").lower()
if ans == "c":
    print("Correct ✅")
    point += 1
else:
    print("Wrong ❌")

# Q6
print("\nQ6. Which country invented paper?")
print("(a) Egypt\n(b) China\n(c) Greece\n(d) India")
ans = input("Your answer: ").lower()
if ans == "b":
    print("Correct ✅")
    point += 1
else:
    print("Wrong ❌")

# Q7
print("\nQ7. Which is the fastest land animal?")
print("(a) Cheetah\n(b) Horse\n(c) Pronghorn\n(d) Leopard")
ans = input("Your answer: ").lower()
if ans == "a":
    print("Correct ✅")
    point += 1
else:
    print("Wrong ❌")

# Q8
print("\nQ8. What is the hardest natural substance?")
print("(a) Diamond\n(b) Quartz\n(c) Graphite\n(d) Ruby")
ans = input("Your answer: ").lower()
if ans == "a":
    print("Correct ✅")
    point += 1
else:
    print("Wrong ❌")

# Q9
print("\nQ9. Which ocean is the deepest?")
print("(a) Indian Ocean\n(b) Pacific Ocean\n(c) Atlantic Ocean\n(d) Arctic Ocean")
ans = input("Your answer: ").lower()
if ans == "b":
    print("Correct ✅")
    point += 1
else:
    print("Wrong ❌")

# Q10
print("\nQ10. How many muscles move when we blink?")
print("(a) 150\n(b) 280\n(c) 200\n(d) 100")
ans = input("Your answer: ").lower()
if ans == "c":
    print("Correct ✅")
    point += 1
else:
    print("Wrong ❌")

# Final result
print("\n🎯 Quiz Finished!")
print("Your score:", point, "out of 10")

if point <= 6:
    print("Average score, keep improving 📘")
elif point == 8:
    print("Good score 👍")
elif point == 9:
    print("Very good 🔥")
else:
    print("Perfect score! 🚀")

input("\nPress Enter to exit...")