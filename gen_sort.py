#!/usr/bin/env python3
"""Generate sort solution using selection sort"""

lines = ["# sort 5 digits"]

# Read 5 digits into memory 20-24 (arbitrary location)
for i in range(5):
    lines.append(f"[{20+i}]<I")

# Selection sort: find min 5 times
# For each output position, find and output the minimum, then mark it as "used" (set to 255)

for output_pos in range(5):
    # Find minimum of remaining values
    # Start with first value
    lines.append(f"A<[20]")  # Current min value
    lines.append("B<0")  # Current min index (0-4)
    
    # Check each position 1-4
    for check_pos in range(1, 5):
        # Compare [20+check_pos] with A
        # If [20+check_pos] < A, update A and B
        lines.append(f"C<[{20+check_pos}]")  # Value to check
        
        # Comparison: if C < A, we want to update
        # Use memory to do comparison
        # Set mem[C] = check_pos, then check if mem[A] was set
        lines.append("[300]<255")  # Default value
        lines.append(f"[C]<{check_pos}")  # Mark position C
        lines.append("D<[A]")  # Check if A's position was marked
        
        # If D != 255, it means C <= A, so we might need to update
        # But this doesn't quite work for strict less-than
        
    # Actually, let me use a simpler approach: explicit comparison
    # For 5 elements, I can unroll everything
    
lines = ["# sort 5 digits - counting sort instead"]

# Read digits
for i in range(5):
    lines.append(f"[{i}]<I")

# Initialize counters at positions 48-57 ('0'-'9')
for d in range(ord('0'), ord('9')+1):
    lines.append(f"[{d}]<0")

# Increment lookup at 100-105
for i in range(6):
    lines.append(f"[{100+i}]<{i+1}")

# Count each digit
for i in range(5):
    lines.append(f"A<[{i}]")  # Get digit value
    lines.append("B<[A]")  # Get current count
    lines.append("C<100")  # Base address
    lines.append("D<[C+B]")  # Get count+1
    lines.append("[A]<D")  # Store back

# Output digits in order
# For each digit '0'-'9', output it count times
# Use position 10 to track total outputs
lines.append("[10]<0")  # Output counter

for digit_val in range(ord('0'), ord('9')+1):
    # Get count for this digit
    lines.append(f"A<{digit_val}")  # Digit to output
    lines.append(f"B<[{digit_val}]")  # Count
    
    # Output this digit B times (B can be 0-5)
    # Use a decrement approach
    for rep in range(5):  # Max 5 repetitions
        lines.append("C<B")  # Copy count
        lines.append("D<0")  # Check if count > 0
        lines.append("[400]<0")  # Default to 0 (no output)
        lines.append("[C]<A")  # If C > 0, output digit
        lines.append("E<[400]")  # Get output value
        lines.append("O<E")  # Output
        # Decrement B
        lines.append("[200]<255")  # Decrement lookup: i -> i-1
        for i in range(1, 6):
            lines.append(f"[{200+i}]<{i-1}")
        lines.append("F<[200+B]")  # Decrement
        lines.append("B<F")  # Update count

lines.append("Z<1")

with open('/workspace/problem_008/code/2282.mv', 'w') as f:
    f.write('\n'.join(lines))

print(f"Generated sort solution with {len(lines)} lines")
