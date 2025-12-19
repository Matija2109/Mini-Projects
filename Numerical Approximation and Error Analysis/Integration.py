"""

IDEAS AND TO-DOS



"""
from numpy.ma.testutils import approx
from pygame.draw import circle


class Integrator:
    def __init__(self, f, a, b):
        self.f = f
        self.a = a
        self.b = b


    def riemann_left(self, n):
        delta_x = (self.b - self.a) / n
        area = 0.0

        for k in range(0, n):
            x = self.a + k * delta_x
            area += self.f(x)

        return area * delta_x


    def riemann_right(self, n):
        delta_x = (self.b - self.a) / n
        area = 0.0

        for k in range(0, n):
            x = self.a + (k + 1) * delta_x
            area += self.f(x)

        return area * delta_x


    def midpoint_method(self, n):
        delta_x = (self.b - self.a) / n
        area = 0.0

        for k in range(0, n):
            m = self.a + (k + 0.5) * delta_x
            area += self.f(m)

        return area * delta_x


    def trapezoid_rule(self, n):
        delta_x = (self.b - self.a) / n
        area = 0.0

        for k in range(0, n):
            a = self.a + k * delta_x
            b = self.a + (k + 1) * delta_x
            area += (b - a) * ((self.f(a) + self.f(b)) / 2)

        return area


def f(x):
    return x**2

I = Integrator(f, 0, 1)

approx_1 = I.riemann_left(1000000)
approx_2 = I.riemann_right(1000000)
approx_3 = I.midpoint_method(1000000)
approx_4 = I.trapezoid_rule(1000000)
exact = 1/3

approximations = [approx_1, approx_2, approx_3, approx_4]
errors = []

for approximation in approximations:
    error = abs(approximation - exact)
    errors.append(error)

print(f"Riemann left {approx_1}, where error is {errors[0]}")
print(f"Riemann right {approx_2}, where error is {errors[1]}")
print(f"Midpoint method {approx_3}, where error is {errors[2]}")
print(f"Trapezoid rule {approx_4}, where error is {errors[3]}")






