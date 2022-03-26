from py_currency_converter import convert

def detect_currency(a):
    f=""
    if a=="dollar":
        f="USD"
    elif a=="pound":
        f="EGP"
    elif a=="Saudi riyals":
        f="SAR"
    elif a=="euro":
        f="EUR"
    return f

def extract_currency(text):
    text=text.split(" ")
    word_from=text[2]
    word_to=text[-1]
    return word_from,word_to
    
def currency(text,amount):
    
    
    word_from,word_to=extract_currency(text)
    base=detect_currency(word_from)
    to=detect_currency(word_to)
    res=convert(base=base,amount=amount,to=[to])
    return str(res[to])

gg=currency("convert from dollar to pound",1)






