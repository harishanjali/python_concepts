# if there is an syntax,logical,run time error then it will crash the app.
# so in order to manage this we have exception handling
#lets see the example

try:
    numerator = int(input('enter numerator: '))
    denominator = int(input('enter denominator: '))
    res = numerator/denominator
    print(res)
except ZeroDivisionError:
    print('denominator should be greater than 0')
except ValueError:
    print('values should be integers not string(characters)')
except Exception:
    #if any error does not matches it comes to this
    print('something went wrong')
else:
    #if it is success then only comes to else block
    print('else block')
finally:
    print('mandatory statements')