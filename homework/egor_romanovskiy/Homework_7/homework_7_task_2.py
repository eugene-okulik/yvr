words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for item in words.items():
    key, value = item
    print(key*value)
    