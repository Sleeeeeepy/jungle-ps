document = input()
pattern = input()
count = 0

i = 0
while i < len(document):
    pattern_found = True
    for j in range(len(pattern)):
        if i + j >= len(document):
            pattern_found = False
            break
        if document[i + j] == pattern[j]:
            continue
        else:
            pattern_found = False
            break
    
    if pattern_found:
        i += len(pattern)
        count += 1
    else:
        i += 1

print(count)