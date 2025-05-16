def is_palindrom(s):
    s= s.lower().replace(" ","")
    return s == s[::-1]

# Example

print(is_palindrom("racecar"))