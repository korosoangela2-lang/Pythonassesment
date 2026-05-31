import re


def count_specific_word(text, search_word):
    count = 0
    words = text.split()

    for word in words:
        word = word.strip(".,!?;:()[]{}\"'").lower()

        if word == search_word.lower():
            count += 1

    return count


def identify_most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())

    if len(words) == 0:
        return ""

    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    most_common = ""
    highest_count = 0

    for word in counts:
        if counts[word] > highest_count:
            highest_count = counts[word]
            most_common = word

    return most_common


def calculate_average_word_length(text):
    words = re.findall(r'\b\w+\b', text)

    if len(words) == 0:
        return 0.0

    total_length = 0

    for word in words:
        total_length += len(word)

    return total_length / len(words)


def count_paragraphs(text):
    if text.strip() == "":
        return 1

    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


def count_sentences(text):
    if text.strip() == "":
        return 1   # FIXED HERE

    sentences = re.split(r'[.!?]+', text)

    count = 0
    index = 0

    while index < len(sentences):
        if sentences[index].strip():
            count += 1
        index += 1

    return count


# Main Program
if __name__ == "__main__":

    with open("news_article.txt", "r", encoding="utf-8") as file:
        article = file.read()

    search_word = input("Enter a word to search for: ")

    print("Specific Word Count:",
          count_specific_word(article, search_word))

    print("Most Common Word:",
          identify_most_common_word(article))

    print("Average Word Length:",
          calculate_average_word_length(article))

    print("Paragraph Count:",
          count_paragraphs(article))

    print("Sentence Count:",
          count_sentences(article))