#!/usr/bin/env python3
"""Generate printf solution - simpler approach"""

lines = ["# printf"]

lines.append("A<I")  # Read input

# Create lookup tables for all 256 values
# Each value i gets encoded as 3-byte string at positions 3*i, 3*i+1, 3*i+2
# But we only have 512 bytes, so we can fit 170 values
# Let's use a different approach: output each digit by checking value ranges

# Simpler: for each of 256 values, compute the output string
# Store hundreds/tens/ones separately

# Ones digit table
for i in range(256):
    lines.append(f"[{i}]<{48 + (i % 10)}")
lines.append("B<[A]")  # B = ones

# Tens digit table (reuse memory)
for i in range(256):
    lines.append(f"[{i}]<{48 + ((i // 10) % 10)}")
lines.append("C<[A]")  # C = tens

# Hundreds digit table
for i in range(256):
    lines.append(f"[{i}]<{48 + (i // 100)}")
lines.append("D<[A]")  # D = hundreds

# Now output with conditional logic
# Setup: mem[48] = 0 (for '0'), mem[other] = value
lines.append("[48]<0")  # Map '0' to 0 (no output)
lines.append("[49]<49")  # Map '1' to '1'
lines.append("[50]<50")  # Map '2' to '2'

# Output hundreds
lines.append("E<[D]")
lines.append("O<E")

# For tens: output if non-zero OR if hundreds was non-zero
# Check if we output hundreds
lines.append("F<D")
lines.append("F<48")  # F = D - 48
lines.append("[400]<C")  # Default to output tens
lines.append("[F]<0")  # If F == 0 (D was '0'), check tens
lines.append("G<[400]")

# Actually, let me use even simpler logic: just always check both conditions
# If hundreds == '0', use conditional for tens
# If hundreds != '0', always output tens

# This is getting messy. Let me just output based on value lookup
lines.append("H<[C]")  # Map tens through lookup
lines.append("J<E")  # J = E (hundreds output)
# If E was 0, check if C should be output
lines.append("[401]<0")
lines.append("[J]<[C]")  # If J != 0, get C
lines.append("K<[401]")
lines.append("L<K")
lines.append("L<H")
lines.append("O<L")

# Always output ones
lines.append("O<B")

lines.append("Z<1")

with open('/workspace/problem_008/code/2280.mv', 'w') as f:
    f.write('\n'.join(lines))

print(f"Generated printf solution with {len(lines)} lines")
