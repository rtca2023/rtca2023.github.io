
def der(rat):
    p = rat.numerator()
    q = rat.denominator()
    return (p.derivative()*q - p*q.derivative())/q^2

def intpoly(p):
    x = p.parent().gen()
    q = 0
    for i in range(p.degree() + 1):
        q += p[i]/(i+1)*x^(i+1)
    return q

def split(p):
    if p.degree() == 0:
       return (p, 1, 1)
    q = p.factor()
    m = max([e for (_, e) in q])
    u = prod([u^e for (u, e) in q if e < m])
    v = prod([u for (u, e) in q if e == m])
    return (u, v, m)

def solvemod(a, u, v):
    # find b with deg(b)<v and a=b*u mod v, assuming gcd(u, v)=1
    g, b, c = u.xgcd(v) # g = b*u + c*v
    assert(g == b*u + c*v)
    b, c = b*a//g, c*a//g # a = b*u + c*v
    assert(a == b*u + c*v)
    b = b % v #   = (b-p*v)*u + (c+p*u)*v
    assert((a - b*u) % v == 0)
    assert(b.degree() < v.degree())
    return b

def hermite(rat):
    p = rat.numerator()
    q = rat.denominator()
    g, p = p.quo_rem(q)
    if g != 0: # polynomial part
        g0, h = hermite(p, q)
        return (intpoly(g) + g0, h)
    # now p/q is a proper ratfun
    u, v, m = split(q) # q = u*v^m
    if m == 1:
        return (0, rat) # done
    else:
        # p/q = D(b/v^(m-1)) + c/(u*v^(m-1))
        b = solvemod(p, -(m-1)*u*v.derivative(), v)
        g, h = hermite(rat - der(b/v^(m-1)))
        return (g + b/v^(m-1), h)

def sqfp(p):
    return p//p.gcd(p.derivative())

def horowitz(rat):
    p = rat.numerator()
    q = rat.denominator()
    g, p = p.quo_rem(q)
    if g != 0: # polynomial part
        g0, h = horowitz(p, q)
        return (intpoly(g) + g0, h)
    # now p/q is a proper ratfun
    gden = q.gcd(q.derivative()) # denominator of g
    hden = q//gden # denominator of h
    gnum = [(q*der(x^i/gden)).numerator() for i in range(gden.degree())]
    hnum = [(q*x^i/hden).numerator() for i in range(hden.degree())]
    d = q.degree()
    sol = matrix([[u[i] for u in gnum + hnum] for i in range(d)]).solve_right(vector([p[i] for i in range(d)]))
    return (sum(sol[i]*x^i for i in range(len(gnum)))/gden, sum(sol[len(gnum)+i]*x^i for i in range(len(hnum)))/hden)

def logpart(rat):
    p = rat.numerator()
    q = rat.denominator()
    assert(p.degree() < q.degree()) # proper ratfun
    assert(q.gcd(q.derivative()) == 1) # squarefree denominator

    C = p.parent().base_ring()
    x, c = C[p.parent().gen(), 'c'].gens()
    out = []
    for u, _ in q.resultant(p - c*q.derivative()).factor():
        out.append((u, C['c'].quotient(u)[x](q).gcd(p - c*q.derivative())))
    return out

