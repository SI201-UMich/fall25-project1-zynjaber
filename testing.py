# Name: Zayn Jaber
# Student ID: 43767236
# Email: zynjaber@umich.edu
# Collaborators: me
# GenAI Tools: ChatGPT (used to assist with code structure, debugging, and explaining concepts I didn’t fully understand)
# Functions created by: Zayn Jaber

import unittest

from main import (
    calculate_avg_body_mass_by_species_and_sex,
    calculate_avg_flipper_length_by_island_and_species
)


class TestPenguinFunctions(unittest.TestCase):


    def test_body_mass_normal(self):
        fake_data = [
            {"species": "Adelie", "sex": "male", "body_mass_g": "4000", "island": "Torgersen"},
            {"species": "Adelie", "sex": "female", "body_mass_g": "3500", "island": "Torgersen"},
        ]
        result = calculate_avg_body_mass_by_species_and_sex(fake_data)
        self.assertAlmostEqual(result["Adelie"]["male"], 4000.0, places=2)
        self.assertAlmostEqual(result["Adelie"]["female"], 3500.0, places=2)

    def test_flipper_length_normal(self):
        fake_data = [
            {"island": "Biscoe", "species": "Gentoo", "flipper_length_mm": "210"},
            {"island": "Biscoe", "species": "Gentoo", "flipper_length_mm": "230"},
        ]
        result = calculate_avg_flipper_length_by_island_and_species(fake_data)
        self.assertAlmostEqual(result["Biscoe"]["Gentoo"], 220.0, places=2)


    def test_body_mass_missing_values(self):
        fake_data = [
            {"species": "Adelie", "sex": "male", "body_mass_g": ""},
            {"species": "Adelie", "sex": "", "body_mass_g": "3700"}
        ]
        result = calculate_avg_body_mass_by_species_and_sex(fake_data)
        self.assertEqual(result, {}) 

    def test_flipper_length_invalid_numbers(self):
        fake_data = [
            {"island": "Dream", "species": "Chinstrap", "flipper_length_mm": "not_a_number"}
        ]
        result = calculate_avg_flipper_length_by_island_and_species(fake_data)
        self.assertEqual(result, {})   

if __name__ == "__main__":
    unittest.main()
