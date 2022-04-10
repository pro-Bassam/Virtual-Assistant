def math(text):
    text = text.split(" ")
    return text


def calculate(text):
    text = math(text)
    result = 0
    if text[1] == "+" or text[1] == "plus":
        result = int(text[0])+int(text[-1])
    elif text[1] == "-" or text[1] == "Subtract" or text[1] == "minus":
        result = int(text[0])-int(text[-1])
    elif text[1] == "*" or text[1] == "multiplied" or text[1] == "multiply" or text[1] == "x":
        result = int(text[0])*int(text[-1])
    elif text[1] == "/" or text[1] == "divided":
        result = int(text[0])/int(text[-1])
    elif text[1] == "**" or text[1] == "power" or text[1] == "-power":
        result = int(text[0])**int(text[-1])

    return str(result)
