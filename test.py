import unittest
import laes
import opret
import delete

class TestEmployee(unittest.TestCase):
    def test_read_all_employees(self):
        medarbejdere = laes.read_all_medarbejdere()
        self.assertEqual(len(medarbejdere), 3)
    
    def test_add_and_delete_employee(self):
        medarbejdere = laes.read_all_medarbejdere()
        self.assertEqual(len(medarbejdere), 3)
        opret.opret_medarbejder("TestName", "TestAfdeling", "test@example.com")
        medarbejdere = laes.read_all_medarbejdere()
        self.assertEqual(len(medarbejdere), 4)
        delete.delete_medarbejder("5")
        medarbejdere = laes.read_all_medarbejdere()
        self.assertEqual(len(medarbejdere), 3)


if __name__ == '__main__':
    unittest.main()