#   I ended writing three separate "programs" when it should've been one whole program with different functions working in conjunction
#   I realize that now but all of the tasks' "programs" work perfectly. Just comment the other programs out when wanting to run a 
#   program. 




# Task 1: Keyword Highlighter
# Write a program that searches through reviews list and looks for
# keywords such as "good", "excellent", "bad", "poor", and "average".
# We want you to capitalize those keywords then print out each review.
# Print out each review with the keywords in uppercase so they stand out.

# reviews = [
#         "This product is really good. I'm impressed with its quality.",
#         "The performance of this product is excellent. Highly recommended!",
#         "I had a bad experience with this product. It didn't meet my expectations.",
#         "Poor quality product. Wouldn't recommend it to anyone.",
#         "The product was average. Nothing extraordinary about it."
#         ]

# word1 = 'good'
# word2 = 'excellent'
# word3 = 'bad'
# word4 = 'poor'
# word5 = 'average'

# for review in reviews:
#     if word1 in review.lower():
#         review_upper = review.replace(word1, word1.upper())
#         print(review_upper)
# for review in reviews:
#     if word2 in review:
#         review_upper = review.replace(word2, word2.upper())
#         print(review_upper)
# for review in reviews:
#     if word3 in review:
#         review_upper = review.replace(word3, word3.upper())
#         print(review_upper)
# for review in reviews:
#     if word4 in review:
#         review_upper = review.replace(word4, word4.upper())
#         print(review_upper)
# for review in reviews:
#     if word5 in review:
#         review_upper = review.replace(word5, word5.upper())
#         print(review_upper)



# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review.
# The function should return the total count of positive and negative words.

# reviews = [
#         "This product is really good. I'm impressed with its quality.",
#         "The performance of this product is excellent. Highly recommended!",
#         "I had a bad experience with this product. It didn't meet my expectations.",
#         "Poor quality product. Wouldn't recommend it to anyone.",
#         "The product was average. Nothing extraordinary about it."
# ]

# def words_in_list(words, reviews):
#     word_counts = {word: 0 for word in words}
    
#     for string in reviews:
#         string = string.lower()
#         for word in words:
#             word_counts[word] += string.count(word.lower())
    
#     return word_counts

# positive_words = ["good", "excellent"]
# negative_words = ["bad", "poor", "average"]
# positive_result = words_in_list(positive_words, reviews)
# negative_result = words_in_list(negative_words, reviews)

# print(f"Here are all of the ocurrences of positive words: {positive_result}")
# print(f"Here are all of the ocurrences of negative words: {negative_result}")

# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary.
# Ensure that the summary does not cut off in the middle of a word.
# step 1 extract the first 30 characters from a review.
# step 2 append "..." to create a summary.


reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
]

def first_30_chars(strings):
    result = []
    
    for string in strings:
        snippet = string[:30]
        if len(string) > 30:
            i = 30
            while i < len(string) and not string[i].isspace():
                snippet += string[i]
                i += 1
            snippet += "..."
        
        result.append(snippet)
    
    return result

result = first_30_chars(reviews)
for review in result:
    print(review)

