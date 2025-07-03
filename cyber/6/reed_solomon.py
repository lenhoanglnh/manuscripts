class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def encode(m1: float, m2: float, m3: float):
    f = lambda x: m1 + m2 * x + m3 * x**2
    return [f(x) for x in range(1, 6)]

def lagrange_basis(p: Point, q1: Point, q2: Point):
    coef = p.y / (p.x - q1.x) / (p.x - q2.x)
    m1 = coef * q1.x * q2.x
    m2 = - coef * (q1.x + q2.x) 
    m3 = coef
    return m1, m2, m3

def decode(p1: Point, p2: Point, p3: Point):
    if isinstance(p1, tuple):
        p1 = Point(*p1)
    if isinstance(p2, tuple):
        p2 = Point(*p2)
    if isinstance(p3, tuple):
        p3 = Point(*p3)
    m_1 = lagrange_basis(p1, p2, p3)
    m_2 = lagrange_basis(p2, p1, p3)
    m_3 = lagrange_basis(p3, p1, p2)
    return m_1[0] + m_2[0] + m_3[0], m_1[1] + m_2[1] + m_3[1], m_1[2] + m_2[2] + m_3[2]

class F4:
    def __init__(self, a, b):
        """ Writes self = a + bk, where k is the imaginary number
        verifying k**2 = 1 + k """
        self.a = a % 2
        self.b = b % 2

    def __add__(self, other: "F4"):
        return F4((self.a + other.a) % 2, (self.b + other.b) % 2)

    def __mul__(self, other: "F4"):
        return F4(
            (self.a * other.a + self.b * other.b) % 2, 
            (self.a * other.b + self.b * other.a + self.b * other.b) % 2
        )

    def __repr__(self):
        return f"{self.a}{self.b}"

    @classmethod
    def all(cls):
        return [F4(0,0), F4(0,1), F4(1,0), F4(1,1)]

class F4Polynomial:
    def __init__(self, m1: F4, m2: F4):
        self.m1 = m1 if isinstance(m1, F4) else F4(*m1)
        self.m2 = m2 if isinstance(m2, F4) else F4(*m2)

    def __call__(self, x: F4):
        x = x if isinstance(x, F4) else F4(*x)
        return self.m1 + (self.m2 * x)

    def sample(self):
        return [self(x) for x in F4.all()]

    def __repr__(self):
    	return f"{self.m1} {self.m2} -> " + " ".join([repr(y) for y in self.sample()])


def print_rs_code():
	for m1 in F4.all():
		for m2 in F4.all():
			print(F4Polynomial(m1, m2))

