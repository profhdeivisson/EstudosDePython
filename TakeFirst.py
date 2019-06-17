#Eis o código

class TakeFirst():
    def __call__(self, values):
        for value in values:
            if value is not None and value != '':
                return value

take_first = TakeFirst()

print(take_first(str(50)))
