from collections import Counter

countries = ["Egypt", "Libya", "Tunisia", "Morocco",
"Egypt", "Spain", "Egypt", "Libya"]

counter = Counter(countries)
print(counter)
print(counter.most_common())