for char in "Rudra":
	print(char)

info = {
	'name' : "Rudra",
	"role": "Dev"
}

for key in info.values():
	print(key)


fruits = ["apple", "orange", "litchi"]

for index in range(len(fruits)):
	print(index, fruits[index])

for index, fruit in enumerate(fruits):
	print(index, fruit)



square = [n * n for n in range(10)]

print(square)

fruits = ["apple", "banana", "kiwi", "pear"]


res = [fruit for fruit in fruits if "a" in fruit]
print(res)

matrix = [[1, 2, 3], [4, 5, 6]]


ans = [num for row in matrix for num in row]
print(ans)

menu = [
	"Masala Chai",
	"Iced Lemon Tea",
	"Green Tea",
	"Iced Peach Tea",
	"Ginger Chai"
];

iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)

words = ["python", "rocks", "hard"]

upper_case = [word.upper() for word in words]

print(upper_case)

names = ["Rudra", "Harman", "Jemmi"]

first_letter_case = [word[0].upper() for word in names]

print(first_letter_case)

res = [word.upper() for word in first_letter_case]

print(res)


# set comprehension

favourite_chais = [
	"Masala Chai", "Green Tea", "Masala Chai", "Lemon Tea", "Green Tea", "Elaichi Chai",
]

unique_chai = { chai for chai in favourite_chais }

print(type(favourite_chais), type(unique_chai))

print(unique_chai)

recipes = {
	"Masala Chai" : ["ginger", "cardamom","clove"],
	"Elaichi chai": ["cardamom", "milk"],
	"Spicy Chai": ["ginger", "black pepper", "clove"]
}


unique_spices = {spice for ingredients in recipes.values() for spice in ingredients};

print(unique_spices)


# dictionary comprehensions

tea_prices_inr = {
	"Masala Chai": 40,
	"Green Tea": 50,
	"Lemon Tea": 200,
}

tea_prices_usd = {tea:price / 80 for tea, price, in tea_prices_inr.items()}

print(tea_prices_usd)



# generator comprehensions

daily_sales = [5, 10, 12, 7, 3, 8 ,9, 15]
total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)
