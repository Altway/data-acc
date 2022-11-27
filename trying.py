import math

def expected_value(k):
    return 2**k*(1-(k/11)) + 1/2*(k/11)

# Log of expected value + starting capital
def expected_utility(start, k):
    return math.log(start+2**k)*(1-(k/11)) + math.log(start+1/2)*(k/11)

# Standard deviation
def riskiness(start, k, expected_take_home):
    return math.sqrt(max(0, (2**k)**2*(1-(k/11)) + (1/2)**2*(k/11)-expected_value(k)**2))


for i in range(11):
    print(f"{riskiness(1, i, 1):.2f}")
