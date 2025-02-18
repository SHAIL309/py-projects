# WORD COUNT
# poem.txt contains famous poem "Road not taken" by poet Robert Frost.
# You have to read this file in your python program and find out words with maximum occurrence.

word_count = {}

with open("poem.txt", "r") as f:
    for line in f:
        words = line.split(" ")
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

print(word_count)

word_occurrences = list(word_count.values())
max_count = max(word_occurrences)
print("Max occurrences of any word is:", max_count)

print("Words with max occurrences are: ")
for word, count in word_count.items():
    if count == max_count:
        print(word)

# STOCK
# stocks.csv contains stock price, earnings per share and book value.
# You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio

with open("stocks.csv", "r") as f, open("Output.csv", "w") as out:
    out.write(f"Company Name, PE Ratio,PB Ratio\n")
    next(f)
    for line in f:
        token = line.split(",")
        company_name = token[0]
        price = float(token[1])
        earnings_per_share = float(token[2])
        book_value = float(token[3])
        pe_ratio = price / earnings_per_share
        price_to_book_ratio = price / book_value
        out.write(f"{company_name},{pe_ratio},{price_to_book_ratio}\n")
