# parenthesis validator :
# str = '{}{}{}(())[{}]' - valid
# str = '{{}}][' - valid
# str = '{}{{' - invalid
# str = '}}}{{{' -valid
# str = '][[][[' - invalid

bracket = {"[":"]","{":"}","(":")","]":"[","}":'{',")":"("}
stack = []

string = input()

for i in string:
    if len(stack) == 0:
        stack.append(i)
    else:
        if bracket[i] in stack:
            stack.remove(bracket[i])
        else:
            stack.append(i)

if len(stack) == 0:
    print(string + " is Valid.")
else:
    print(string + " is inValid.")