import unittest
from app.kml_parser import KmlParser


class Tdd_kml_parser(unittest.TestCase):
 
    
    def test_parser_is_not_None(self):
       
        
        reader = KmlParser()
        obj = reader.parse_kml("CorporateTransport.kml")
        
        self.assertIsNotNone(obj)
    
    
    def test_parser_returns_TYPE(self):
       
        
        reader = KmlParser()
        result = reader.parse_kml("CorporateTransport.kml")
        
        self.assertIsInstance(result, dict)



if __name__ == '__main__':
    unittest.main()