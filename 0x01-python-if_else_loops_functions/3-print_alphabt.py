#!/usr/bin/python3
# Print the ASCII alphabet in lowercase excluding 'q' and 'e' without new lines

for i in range(ord('a'), ord('z') + 1):
    if chr(char) not in {'q', 'e'}:
        print('{:c}'.format(i), end='')
        
