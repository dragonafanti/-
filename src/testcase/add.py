#coding= utf-8
'''
Created on 2015��9��24��

@author: wanglong
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        self._a = 1
        self._b = 2


    def tearDown(self):
        pass
    
    def a_1(self):
        a = 2 
        return a

    def testName(self):
       
        k = Test.a_1(self)
        print ("k="+str(k))
        
        e = self.a_1()
        print "e="+str(e)
        
        c = self._a+self._b
        print c

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()