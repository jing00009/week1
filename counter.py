counter1=0
counter2=0
def case_counter(text):
    counter1=0
    counter2=0
    for charactor in text:
        if charactor.isupper()==True:
            counter1=counter1+1
        elif charactor.islower()==True:
            counter2=counter2+1
    return counter1,counter2
print(
    case_counter("Hello World!")
)  # Expected: Uppercase letters: 2, Lowercase letters: 8
print(case_counter("PYTHON"))  # Expected: Uppercase letters: 6, Lowercase letters: 0
print(case_counter("python"))  # Expected: Uppercase letters: 0, Lowercase letters: 6
print(case_counter("1234!@#$"))  # Expected: Uppercase letters: 0, Lowercase letters: 0
