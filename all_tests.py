import unittest
import os

#ajout de toutes mes fonctions
from reverse_string import reverse_string
from reverse_digits import reverse_digits
from reverse_number import reverse_number

class My_tests(unittest.TestCase):
    #la fonction retourne bien un string
    def test_reverse_string(self):
        print("blabla")
        self.assertEqual(type(reverse_string("maison")),str)
        self.assertEqual(reverse_string("maison"),"nosiam")

if __name__ == '__main__':
    #Verbosity indique le nombre d'info que va retourner l'execution
    #de mes tests
    unittest.main(verbosity=2)