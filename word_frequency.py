from collections import Counter

text = """
AI is transforming the world. Learning AI and coding AI projects can improve your skills.
Python is great for AI and data analysis.
"""

words = text.lower().split()
word_counts = Counter(words)

print("Top 5 words:")
for word, count in word_counts.most_common(5):
    print(f"{word}: {count}")
