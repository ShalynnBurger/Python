# x=3
# print(x) 

# x=10
# if x >50:
#     print("bigger than 50")
# else:
#     print("smaller than 50")    


# Practice Challenge: Correct the errors!
first_name = "Alana"
last_name = "Da Silva"
age = 36
profession = "Software Developer"
years_experience = 5

greeting = "Hello my name is "

print(f"Hello my name is {first_name} {last_name}.") 
# Desired output: Hello my name is Alana Da Silva

print(f"I am {age} years old") 
# Desired output: I am 36 years old

print(f"I work as a {profession}.")
# Desired output: I work as a Software Developer.

exp_string = "I have worked in the field for {} years."
print(exp_string.format(years_experience))
# Desired output: I have worked in the field for 5 years.

start_age = age - years_experience 
print(f"I started in the field when I was {start_age} years old.")
# Desired output: I started in the field when I was 31 years old.