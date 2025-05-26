#!/usr/bin/python3
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

original_x = x

html = f"""
<html><body><h2>Assignment #3 - Python Script Result</h2>
<p>Original Values: x={original_x}, y={y}, z={z}</p>
"""

x += y
html += f"<p>After x += y: {x}</p>"

x -= z
html += f"<p>After x -= z: {x}</p>"

x *= y
html += f"<p>After x *= y: {x}</p>"

x %= z
html += f"<p>After x %= z: {x}</p>"

if z != 0:
    x /= z
    html += f"<p>After x /= z: {x}</p>"
else:
    html += "<p>Division by zero avoided.</p>"

result = x + y + z
html += f"<p>Final Result: x + y + z = {x} + {y} + {z} = {result}</p></body></html>"

print(html)
