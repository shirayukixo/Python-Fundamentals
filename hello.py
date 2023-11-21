#name = input("What is your name? ")

#print(f"Hello, {name}")

date = "14/11/1994"
first_slash_index = date.find("/")
second_slash_index = date.find("/", first_slash_index + 1)
birth_date = date[:first_slash_index]
birth_month = date[first_slash_index + 1:second_slash_index]
birth_year = date[second_slash_index + 1:]
milennium = date[second_slash_index + 1] + "000"
print(birth_date)
print(birth_month)
print(birth_year)
print(milennium)