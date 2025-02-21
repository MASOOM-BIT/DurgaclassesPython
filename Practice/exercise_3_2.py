def do_twice(print_spam,value):
    print_spam(value)
    print_spam(value)

def print_spam(value):
    print('spam',value)

do_twice(print_spam,56)