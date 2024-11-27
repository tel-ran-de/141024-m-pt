class A(object): pass
class B(object): pass
class C(A): pass
class D(A): pass
class E(C, D): pass
class F(B): pass
class G(B): pass
class H(F, G): pass
class I(E, H): pass


print(I.mro())