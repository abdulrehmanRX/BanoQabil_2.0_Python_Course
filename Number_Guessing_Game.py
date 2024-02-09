while True:
    input()
    print("Welcome to the country guess game ")
    print("22334")
    key = 22334
    user = int(input("Enter the given number for verification are you human or not"))
    if user == key:
        print("verified")
        break
    else:
        print("not verify")
input("Press enter key")

score = 0


#Q1    
lis = ['canada','china','Pakistan']
print("welcome to Global Mystery Quest: Country Guess")
print("choose correct country from question given blow")
print("Q1:  Which are the most populated country?")
for x in lis:
    print(x)
user1 = input(".")
if user1 == lis[1]:
    print("correct")
    score += 1
else:
    print("wrong")
input("Press enter key")

#Q2
lis1 = ['China','Russia','Canada','United States'] 
print("Which country is the largest by land area?")
for x in lis1:
    print(x)
user1 = input(".")
if user1 == lis1[1]:
    print("correct")
    score += 1
else:
    print("wrong")
input("Press enter key")


#Q3
lis2 = [ 'Italy','Spain','France','Germany'] 
print("Which country is famous for the Eiffel Tower?")
for x in lis2:
    print(x)
user1 = input(".")
if user1 == lis2[2]:
    print("correct")
    score += 1
else:
    print("wrong")  
input("Press enter key")


#Q4
lis3 = [ 'Russia','Germany','Italy','France'] 
print("Which country is located in both Europe and Asia?")
for x in lis3:
    print(x)
user1 = input(".")
if user1 == lis3[0]:
    print("correct")
    score += 1
else:
    print("wrong")
input("Press enter key")


#Q5
lis4 = [ 'Argentina','Colombia','Brazil','Venezuela'] 
print("Which country is famous for its Carnival celebration in Rio de Janeiro?")
for x in lis4:
    print(x)
user1 = input(".")
if user1 == lis4[2]:
    print("correct")
    score += 1
else:
    print("wrong")
input("Press enter key")


#Q6
lis5 = [  'South Africa','Tanzania','Kenya','Botswana'] 
print("Which country is famous for its Maasai Mara National Reserve?")
for x in lis5:
    print(x)
user1 = input(".")
if user1 == lis5[2]:
    print("correct")
    score += 1
else:
    print("wrong")
input("Press enter key")

print("Thanks for playing the game")
print("Your score is 6 out of",score)

input("Press any key to turn off")