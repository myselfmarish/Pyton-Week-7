# this is a comment
# this is a print method. Print will echo out anything inside the () round brackets to the terminal, when we run the file.
print("This is my first python script!!!")

# variavles are placeholders, with dynamic values -> things that can change 
#they get stored in memory and refernced later
name = "Masha"
age = 19
eyecolor = "brown"
haircolor = "brown"

# Arrays are variables on steriods. They let us store many values in one
# variable -> to help us group data.
# This makes our scripting files easier to understand and work it.

# car1 = "Volvo"
# car2 = "Toyota"
# car3 = "Fiesta"
cars = ["Volvo", "Toyota", "Fiesta"]

print("My name is " + name)


# input is another Python "thing" - it waits with a flashing cursor
# until yoy type something and hite enter
alternateName = input("What is YOUR name?")

print ("Ma name is now " + alternateName)

print("My age is " + str(age))