greetings = ['Hello', 'Bonjour']

for greeting in greetings:
    print(f"{greeting}, World!")


def mystery():
    num = 10 * 3

    if num == 10:
        num = num * 10
    elif num == 30:
        num = num * 30

    return num


print(mystery())
