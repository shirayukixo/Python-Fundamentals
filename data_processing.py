a = input("Please enter a sentence: ")
print(a.upper())

b = input("Please enter a paragraph: ")
b_formatted = len(b.split())
print(f"The paragraph has {b_formatted} words.")

c = input("Please enter a string: ")
c_formatted = any(chr.isdigit() for chr in c)
print(c_formatted)

d = input("Please enter another string: ")
d_formatted = d.replace("a", "o")
print(d_formatted)

e = input("Please enter your full name: ")
e_formatted = e.split()
e_final = [name[0].upper() for name in e_formatted]
print(f"Your inititals are: {''.join(e_final)}")

f = input("Please enter one more string: ")
print(f"The length of your string is: {len(f)}")