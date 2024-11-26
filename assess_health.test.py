import unittest

class TestAssessHealth(unittest.TestCase):
    def test_status(self):
        self.assertEqual(assess_health(90, 111), 'Status')  

    def test_risk(self):
        self.assertEqual(assess_health(120, 129), 'Risk') 

    def test_high_risk_level_1(self):
        self.assertEqual(assess_health(150, 150), 'High Risk level 1')  

    def test_high_risk_level_2(self):
        self.assertEqual(assess_health(180, 160), 'High Risk level 2')

    def test_high_risk_level_3(self):
        self.assertEqual(assess_health(185, 170), 'High Risk level 3') 

    def test_out_of_range(self):
        self.assertEqual(assess_health(200, 190), 'Out of range')  

if __name__ == '__main__':
    unittest.main()
