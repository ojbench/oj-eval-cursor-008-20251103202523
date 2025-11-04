#!/usr/bin/env python3
"""Generate .mv solutions for all problems"""

def gen_hello():
    """2276 - Hello World"""
    s = "Hello World!"
    lines = [f"# Hello World"]
    for ch in s:
        lines.append(f"O<{ord(ch)}")
    lines.append("Z<1")
    return '\n'.join(lines)

def gen_ifelse():
    """2277 - if else"""
    lines = [
        "# if else",
        "A<I",
        "B<I",
        "[0]<48",
        "[1]<49",
        "[A]<1",
        "C<[B]",
        "D<[C]",
        "O<D",
        "Z<1"
    ]
    return '\n'.join(lines)

def gen_increment():
    """2278 - i++"""
    lines = ["# i++"]
    # Lookup table for digit increment
    for i in range(ord('0'), ord('9')):
        lines.append(f"[{i}]<{i+1}")
    lines.append(f"[{ord('9')}]<{ord('0')}")
    lines.append("A<I")
    lines.append("B<[A]")
    lines.append("O<B")
    lines.append("Z<1")
    return '\n'.join(lines)

def gen_echo():
    """2279 - echo"""
    lines = [
        "# echo",
        "A<I",
        "O<A",
        "[0]<0",
        "[A]<1",
        "B<[0]",
        "Z<B"
    ]
    return '\n'.join(lines)

def gen_printf():
    """2280 - printf - output ASCII code"""
    lines = ["# printf"]
    
    # Simple approach: create lookup tables for all 256 values
    # Store hundreds at 300+i, tens at 400+i, ones at 500+i
    # But memory is only 512, so we need a different approach
    
    # Use subtraction loops instead
    lines.append("A<I")  # Read input
    lines.append("B<A")  # Save original
    
    # Compute hundreds digit
    lines.append("C<0")  # hundreds = 0
    lines.append("D<100")  # threshold
    
    # If A >= 100, increment C
    lines.append("[256]<0")  # default
    lines.append("[257]<1")  # marker
    # This is getting complex again
    
    # Let me use a simpler approach: just handle common ASCII range
    # For '9' (57), output '5' (53) then '7' (55)
    
    # Create lookup tables at positions 256-511
    # Actually, let's just create inline computation
    
    lines.append("Z<1")
    return '\n'.join(lines)

def gen_sort():
    """2282 - sort 5 digits"""
    lines = ["# sort"]
    # Read into mem 0-4
    for i in range(5):
        lines.append(f"[{i}]<I")
    
    # Simple selection sort: 5 passes, each finds and outputs the min
    # For each output position, scan for minimum and output it
    
    # This is still complex. Let me use a counting sort instead
    # Initialize counters
    for d in range(ord('0'), ord('9')+1):
        lines.append(f"[{d}]<0")
    
    # Count each digit
    for i in range(5):
        # Read digit from position i, increment its counter
        # This needs increment logic
        pass
    
    lines.append("Z<1")
    return '\n'.join(lines)

# Generate all solutions
with open('/workspace/problem_008/code/2276.mv', 'w') as f:
    f.write(gen_hello())

with open('/workspace/problem_008/code/2277.mv', 'w') as f:
    f.write(gen_ifelse())

with open('/workspace/problem_008/code/2278.mv', 'w') as f:
    f.write(gen_increment())

with open('/workspace/problem_008/code/2279.mv', 'w') as f:
    f.write(gen_echo())

print("Generated solutions for 2276-2279")
