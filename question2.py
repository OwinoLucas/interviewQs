# Question 2

def transformed_String(word):
    divide = [char for char in word]
    divide.reverse()
    divide = ''.join(divide)
    return divide


word = 'lorem at'
print(transformed_String(word))
