import re


def clean_name(name):
    """
    ' sveta ' --> 'Sveta'
    """
    return name.strip().capitalize()


def make_username(first, last):
    """
    'Sveta ' ' Svetlaya ' --> sveta_svetlaya
    """
    return f"{first.strip()}_{last.strip()}".lower()


# Примеры работы функций:
if __name__ == "__main__":
    print(clean_name(" sveta "))
    print(make_username("Sveta ", " Svetlaya "))

def is_valid_email(email):
    if "@" not in email:
        return False
    domain = email.split("@")[-1]
    return "." in domain

def is_valid_email_second(email):
    pattern = r"^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def is_valid_password(password):
    if len(password) >= 8:
        return True
    return False

def cut_length(text, limit):
    if len(text) > limit:
        return text[:limit] + "***"
    return text

def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count

def initials(full_name):
    if not full_name.strip():
        raise ValueError("Input is empty")
    parts = full_name.split()
    initials = [part[0].upper() for part in parts]
    return ".".join(initials)+"."