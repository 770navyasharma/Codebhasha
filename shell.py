import codebhasha

while True:
    text = input('codebhasha >> ')
    result, error = codebhasha.run('<stdin>', text)
    
    if error:
        print(error.as_string())
    elif(result):
        print(result) 