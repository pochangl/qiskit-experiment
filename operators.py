
def add(c, a, b, sum, carry):
    c.reset(sum)
    c.reset(carry)
    c.cx(a, sum)
    c.cx(b, sum)
    c.ccx(a, b, carry)
