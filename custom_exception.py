#custom exception comes into picture when computer cannot recognise the problems in your code
#for example simple interest
#we dont give minus values to p,t,r right? so we will raise error when they give minus value

class myException(Exception):
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):
        return (self.msg)

    def infomsg(self):
        return 'log inserted to Db'

try:
    p = int(input('Enter principle: '))
    t = int(input('enter time: '))
    r = int(input('enter roi: '))

    if p<0 or t<0 or r<0:
        raise myException('Values should greater than 0')
    else:
        si = (p*t*r)/100
        print(si)
except myException as obj:
    print(obj)
    print(obj.infomsg())
except ValueError:
    print('values should be integers')
else:
    print('done')
finally:
    print('mandatory statements')
