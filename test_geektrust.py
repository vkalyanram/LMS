import unittest
from geektrust import LMS
class TestLMSMethods(unittest.TestCase):

    def test_add_course(self):
        obj=LMS()
        self.assertEqual(obj.add_course('JAVA','INS1',12072022,4,5),'OFFERING-JAVA-INS1')
        self.assertEqual(obj.add_course('ROR','INS2',12072022,4,5),'OFFERING-ROR-INS2')
    def test_get_name_from_email(self):    
        obj=LMS()
        self.assertEqual(obj.get_name_from_email('WOO@GMAIL.COM'),'WOO')
    def test_register_couse(self):
        obj=LMS()
        obj.add_course('JAVA','INS1',12072022,4,5)
        self.assertEqual(obj.register_course('JAVA','WOO@GMAIL.COM'),'REG-COURSE-WOO-JAVA ACCEPTED')    
        self.assertEqual(obj.register_course('JAVA','ABC@GMAIL.COM'),'REG-COURSE-ABC-JAVA ACCEPTED')    
    
if __name__ == '__main__':
    unittest.main()
