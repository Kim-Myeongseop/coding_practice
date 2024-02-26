str = input()
result = ''
for s in str:
    if s.islower():
        result += s.upper()
    elif s.isupper():
        result += s.lower()

print(result)
        
    
