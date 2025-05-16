def reverse_text(text):
    words = text.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)


def reverse_string(s):
    return s[::-1]
# Example
print(reverse_text("Hello"))
print(reverse_string("Hello"))