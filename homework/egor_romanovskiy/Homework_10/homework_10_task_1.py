def finish_me(func):
    def wrapper(x):
        func(x)
        print('finished')
    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
