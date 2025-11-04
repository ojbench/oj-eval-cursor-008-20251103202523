#!/usr/bin/env python3
# Generate printf solution with lookup tables

lines = []
lines.append("# printf - output ASCII code")

# Create lookup tables for digits
# mem[0-99]: ones digit of numbers 0-99
# mem[100-199]: tens digit of numbers 0-99
# mem[200-255]: hundreds digit of numbers 0-255

# Ones digit lookup (0-99)
for i in range(100):
    ones = i % 10
    lines.append(f"[{i}]<{48 + ones}")

# Tens digit lookup (100-199)
for i in range(100):
    tens = (i // 10) % 10
    lines.append(f"[{100 + i}]<{48 + tens}")

# Hundreds digit lookup (200-255)
for i in range(56):  # 0-55 maps to 200-255
    if i < 100:
        hund = 0
    elif i < 200:
        hund = 1
    else:
        hund = 2
    # We'll handle hundreds differently
    
# Read input
lines.append("A<I")

# Determine hundreds digit
lines.append("B<0")  # Default hundreds = 0
lines.append("C<100")
lines.append("D<200")
lines.append("[256]<0")  # Default flag
lines.append("[257]<1")  # Flag for >= 100
lines.append("[258]<2")  # Flag for >= 200

# This is still complex. Let me simplify further.

# Actually, for the contest, I'll create a more straightforward solution
# that handles the specific range of printable ASCII (32-126)

# For now, let me create a simple but long solution

print('\n'.join(lines))
