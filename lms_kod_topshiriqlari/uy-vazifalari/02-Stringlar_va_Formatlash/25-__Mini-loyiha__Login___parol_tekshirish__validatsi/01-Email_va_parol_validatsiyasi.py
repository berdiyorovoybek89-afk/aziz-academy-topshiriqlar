email = input()
parol = input().strip()
valid_email = '@' in email and '.' in email and email == email.lower()
valid_parol = 8 <= len(parol) <= 16
print(valid_email and valid_parol)