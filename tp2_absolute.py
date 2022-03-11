import unittest

def a(i):
    b=0
    if i<=0:
        b=-i
    else:
        b=i
    return b

i=-5
c=a(i)
print (c)

class mytest(unittest.TestCase):
    def test_a(self):
        va=a(-3)
        assert va==3

    def test_a(self):
        va=a(-5)
        assert va==5

if __name__=='__main__':
    unittest.main()
