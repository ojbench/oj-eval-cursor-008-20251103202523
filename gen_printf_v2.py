#!/usr/bin/env python3
"""Generate printf solution - cleaner version"""

lines = ["# printf"]
lines.append("A<I")

# Ones digit lookup
for i in range(256):
    lines.append(f"[{i}]<{48 + (i % 10)}")
lines.append("B<[A]")

# Tens digit lookup (reuse memory)
for i in range(256):
    lines.append(f"[{i}]<{48 + ((i // 10) % 10)}")
lines.append("C<[A]")

# Hundreds digit lookup
for i in range(256):
    lines.append(f"[{i}]<{48 + (i // 100)}")
lines.append("D<[A]")

# Create conditional output mapping at positions 48-57 ('0'-'9')
# '0' -> 0 (no output), others -> themselves
lines.append("[48]<0")
for i in range(49, 58):
    lines.append(f"[{i}]<{i}")

# Output hundreds (using mapping)
lines.append("E<[D]")
lines.append("O<E")

# Output tens conditionally
# If E != 0 (hundreds was output), always output tens
# If E == 0, use conditional mapping for tens
lines.append("[400]<0")  # default
lines.append("[E]<C")  # if E != 0, mem[E] = C
lines.append("F<[400]")  # F = 0 if E was 0
lines.append("G<[C]")  # G = mapped C (0 if C='0')
lines.append("H<F")  # H = F
lines.append("H<G")  # H = G (or F if F != 0)
lines.append("O<H")

# Always output ones
lines.append("O<B")

lines.append("Z<1")

with open('/workspace/problem_008/code/2280.mv', 'w') as f:
    f.write('\n'.join(lines))

print(f"Generated printf solution with {len(lines)} lines")
