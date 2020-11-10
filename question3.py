# Question3
# LCM OF 20/1 and 20/2 will give the highest number of steps
# GCD of 20/1 and 20/2 will give the lowest number of steps
# Factorial of line 2 & 3 gives the possible number of combinations if it takes random steps of 1 or 2
import math
lcm_1, lcm_2 = math.lcm(20, 1),  math.lcm(20, 2)
gcd_1, gcd_2 = math.gcd(20, 1),  math.gcd(20, 2)

highest_step_no = lcm_1 + lcm_2
lowest_step_no = gcd_1 + gcd_2
factorial = 1
factorial1 = 1
# math.factorial(highest_step_no) or
if highest_step_no >= 1:
    for i in range(1, highest_step_no + 1):
        factorial = factorial * i
        return factorial
if lowest_step_no >= 1:
    for i in range(1, lowest_step_no + 1):
        factorial1 = factorial1 * i
        return factorial1

return factorial - factorial1
