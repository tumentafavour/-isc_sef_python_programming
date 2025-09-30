
def is_palindrome(text):
    str_text = str(text)
    if str_text == str_text[::-1]:
        return True
    else:
        return False
    
text = "ekitike"

if is_palindrome((text)):
    print("True.")
else:
    print("False.")
