#первый вариант
def repeat_me(func):
    def wrapper(a, **kwargs):
        for num in range(kwargs.get('count', 1)):
            func(a)
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


#второй вариант
def repeat(count):
    def wrapper1(func):
        def wrapper2(a):
            for num in range(count):
                func(a)
        return wrapper2
    return wrapper1


@repeat(count=2)
def example(text):
    print(text)


example('print me')
