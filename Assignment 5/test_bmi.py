import subprocess
import sys
import unittest



def run_program(user_input):
    result = subprocess.run([sys.executable, "main.py"], input=user_input, capture_output=True, text=True)
    return result


class TestBMI(unittest.TestCase):

    def test1_normal_bmi(self):
        "Test 1: normal (150 lbs, 5 ft 8 in)"
        result = run_program("150\n5\n8\nn\n")
        self.assertIn("22.8", result.stdout)
        self.assertIn("Normal", result.stdout)
        self.assertEqual(result.returncode, 0)

    def test2_underweight_bmi(self):
        "Test 2: underweight (100 lbs, 6 ft 0 in)"
        result = run_program("100\n6\n0\nn\n")
        self.assertIn("13.6", result.stdout)
        self.assertIn("Underweight", result.stdout)
        self.assertEqual(result.returncode, 0)

    def test3_overweight_bmi(self):
        "Test 3: overweight (180 lbs, 5 ft 8 in)"
        result = run_program("180\n5\n8\nn\n")
        self.assertIn("27.4", result.stdout)
        self.assertIn("Overweight", result.stdout)
        self.assertEqual(result.returncode, 0)

    def test4_obese_bmi(self):
        "Test 4: obese (250 lbs, 5 ft 8 in)"
        result = run_program("250\n5\n8\nn\n")
        self.assertIn("38.0", result.stdout)
        self.assertIn("Obese", result.stdout)
        self.assertEqual(result.returncode, 0)

    def test5_letters_for_weight(self):
        "Test 5: letters typed for weight"
        result = run_program("abc\n150\n5\n8\nn\n")
        self.assertIn("Incorrect value: could not convert string to float", result.stdout)
        self.assertIn("22.8", result.stdout)
        self.assertEqual(result.returncode, 0)

    def test6_negative_weight(self):
        "Test 6: negative weight"
        result = run_program("-10\n5\n8\n150\n5\n8\nn\n")
        self.assertIn("Weight must be greater than 0", result.stdout)
        self.assertIn("22.8", result.stdout)
        self.assertEqual(result.returncode, 0)

    def test7_inches_out_of_range(self):
        "Test 7: inches too large"
        result = run_program("150\n5\n15\n150\n5\n8\nn\n")
        self.assertIn("Inches must be 0-11", result.stdout)
        self.assertIn("22.8", result.stdout)
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
