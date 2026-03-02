# Package Sorter - Robotic Arm Dispatch Logic

## Problem
Categorize packages into STANDARD, SPECIAL, or REJECTED based on dimensions and mass.

## Rules
- **Bulky**: volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm
- **Heavy**: mass ≥ 20 kg
- **STANDARD**: not bulky AND not heavy
- **SPECIAL**: bulky OR heavy (but not both)  
- **REJECTED**: bulky AND heavy

## Usage
```python
from solution import sort

# Returns "STANDARD", "SPECIAL", or "REJECTED"
result = sort(width=10, height=10, length=10, mass=5)
