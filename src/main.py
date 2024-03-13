print('Enter text to be echoed back. Enter \'exit\' to quit.')
while True:
    text = input(">: ")
    if text == 'exit':
        exit()
    print(text)