"""
    data annotations: requires python 3.6+
"""
from typing import List

primes: List[int] = [2, 3, 5, 7]

print(primes)
# warning
primes.append("11")
primes.append("foo")
# still ok
print(primes)

