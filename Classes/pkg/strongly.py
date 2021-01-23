"""
    data annotation: requires python 3.6+
"""
from typing import List

primes: List[int] = []

primes.append(2)
primes.append(3)
primes.append(5)
primes.append(7)

print(primes)
# warning
primes.append("11")
primes.append("foo")
# still ok
print(primes)

