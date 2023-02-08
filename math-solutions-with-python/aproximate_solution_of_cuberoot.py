cube = float(input('input a number: '))

guess = 0.0
num_guesses = 0
epsilon = 0.01
increament = 0.01
while abs(guess**3-cube) >= epsilon and guess<=cube:
    guess +=increament
    num_guesses +=1
print('number of guesses: ',num_guesses)
if abs(guess**3-cube) >= epsilon:
    print('failed on cube root of:',cube)
else:
    print(guess,'is close to cube root of',cube)

