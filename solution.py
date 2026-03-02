def sort(width, height, length, mass):
    """
    Sorts packages into STANDARD, SPECIAL, or REJECTED stacks.
    
    Args:
        width: float - width in centimeters
        height: float - height in centimeters  
        length: float - length in centimeters
        mass: float - mass in kilograms
    
    Returns:
        str: "STANDARD", "SPECIAL", or "REJECTED"
    
    Rules:
        - Bulky: volume >= 1,000,000 cm³ OR any dimension >= 150 cm
        - Heavy: mass >= 20 kg
        - STANDARD: not bulky AND not heavy
        - SPECIAL: bulky OR heavy (but not both)
        - REJECTED: bulky AND heavy
    """
    volume = width * height * length
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


# Comprehensive test suite
import unittest

class TestPackageSorter(unittest.TestCase):
    
    def test_standard_small_light(self):
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")
    
    def test_standard_boundary_just_under(self):
        self.assertEqual(sort(99, 100, 100, 19.99), "STANDARD")
        self.assertEqual(sort(149, 100, 100, 19), "STANDARD")
    
    def test_bulky_by_volume_exact(self):
        self.assertEqual(sort(100, 100, 100, 5), "SPECIAL")
    
    def test_bulky_by_volume_over(self):
        self.assertEqual(sort(100, 100, 101, 5), "SPECIAL")
    
    def test_bulky_by_dimension_exact(self):
        self.assertEqual(sort(150, 10, 10, 5), "SPECIAL")
        self.assertEqual(sort(10, 150, 10, 5), "SPECIAL")
        self.assertEqual(sort(10, 10, 150, 5), "SPECIAL")
    
    def test_bulky_by_dimension_over(self):
        self.assertEqual(sort(151, 10, 10, 5), "SPECIAL")
    
    def test_heavy_exact(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
    
    def test_heavy_over(self):
        self.assertEqual(sort(10, 10, 10, 21), "SPECIAL")
    
    def test_rejected_bulky_volume_and_heavy(self):
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
    
    def test_rejected_bulky_dimension_and_heavy(self):
        self.assertEqual(sort(150, 10, 10, 25), "REJECTED")
        self.assertEqual(sort(10, 200, 10, 30), "REJECTED")
    
    def test_floating_point_precision(self):
        self.assertEqual(sort(99.9, 99.9, 99.9, 19.9), "STANDARD")
        self.assertEqual(sort(100.01, 100, 100, 5), "SPECIAL")
        self.assertEqual(sort(10, 10, 10, 19.999), "STANDARD")
    
    def test_zero_and_negative_handling(self):
        self.assertEqual(sort(0, 10, 10, 5), "STANDARD")
        self.assertEqual(sort(10, 10, 10, 0), "STANDARD")


def run_demo():
    """Quick visual verification of key cases"""
    cases = [
        (10, 10, 10, 5, "STANDARD", "small light box"),
        (100, 100, 100, 5, "SPECIAL", "bulky by volume"),
        (150, 10, 10, 5, "SPECIAL", "bulky by dimension"),
        (10, 10, 10, 20, "SPECIAL", "heavy only"),
        (100, 100, 100, 20, "REJECTED", "bulky and heavy"),
        (200, 50, 30, 25, "REJECTED", "large and heavy"),
    ]
    
    print("\n📦 Package Sorter - Quick Verification")
    print("=" * 60)
    for w, h, l, m, expected, desc in cases:
        result = sort(w, h, l, m)
        status = "✓" if result == expected else "✗"
        print(f"{status} {desc:25} | sort({w}, {h}, {l}, {m}) → {result}")
    print("=" * 60)


if __name__ == "__main__":
    # Run demo first for quick visual check
    run_demo()
    
    # Then run full test suite
    print("\n🧪 Running full test suite...")
    unittest.main(argv=[''], verbosity=2, exit=False)
