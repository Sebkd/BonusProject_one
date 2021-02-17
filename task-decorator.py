# test decorator
'''тест для понимания декораторов'''

def simple_decor(func):
    def wrapper():
        print('Run function')
        func()
        print('End function')
    return wrapper

@simple_decor
def test():
    print('Test function')

test()