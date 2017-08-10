"""
The probability that a machine produces a defective product is p.
What is the probability that the 1st defect is found during the first n inspections?
"""


def neg_bernoulli(n, p):
    return p * (1-p)**(n-1)

defective_prob = 1 / 3.0
inspection = 5

prob = sum(neg_bernoulli(i, defective_prob) for i in range(1, 6))
print(round(prob, 3))
