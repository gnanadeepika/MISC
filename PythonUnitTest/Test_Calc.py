import unittest
import Calc

class Test_Calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calc.add(10,5),15 )
        self.assertEqual(Calc.add(10,-10),0)
        self.assertEqual(Calc.add(-2,-1),-3)


    def test_div(self):
        self.assertEqual(Calc.div(10,5),2)
        self.assertEqual(Calc.div(-1,1),-1)
        self.assertEqual(Calc.div(5,2),2.5)
        #self.assertRaises(ValueError,Calc.div,10,0)
        with self.assertRaises(ValueError):
            Calc.div(10,0)

#without __name__ we can run : python -m unittest Test_Calc.py

if __name__=="__main__":
    unittest.main()

#adding __name__ we can normally run code kile python Test_Calc