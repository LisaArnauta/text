def name_number(func):
    def wrapper(arg):
        name_file = arg.replace('.txt','')
        words = arg.count(' ')+1
        print(name_file)
        print(words)

@name_number
def read_print_text (text_file):
    if text_file.endswith('.txt'):
        text_file.read()
        print(text_file)
    else :
        pass

