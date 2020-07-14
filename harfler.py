"""by KubilayKilic"""

from __future__ import print_function, division
import turtle
from cokgen import cember, yay


#ilkellerin tanımlanması, 1.seviye ilkeller
#fd, bk, lt, rt, pu, pd

def fd(t, u):
    t.fd(u)
    
def bk(t, u):
    t.bk(u)

def lt(t, a=90):
    t.lt(a)

def rt(t, a=90):
    t.rt(a)

def pd(t):
    t.pd()

def pu(t):
    t.pu()

#2.seviye ilkeller, 1.seviyenin kombinasyonları
#pre*post condisiton'ları yoktur.

def fdlt(t, n, a=90):
    """ileri ve yukarı"""
    fd(t, n)
    lt(t, a)

def fdbk(t, n):
    "ileri-geri, başlangıç pozisyonuna dönen."
    fd(t, n)
    bk(t, n)

def atla(t, n):
    """kalemi kaldır ve hareket ettir."""
    pu(t)
    fd(t, n)
    pd(t)

def strbas(t, n, a=90):
    """dikey çizci çekip, turtle'ı yukarıda sağa bakar çekilde bırakır."""
    lt(t)
    fd(t, n)
    rt(t, a)

def bos(t, n):
    """turtle'ı dikey kaldırıp yukarıda sağa bakıcak şekilde bırakır."""
    lt(t)
    atla(t, n)
    rt(t)

#3.seviye ilkeller. 1.ve2. seviyedekileri kullanır.
#dikey-yatay elementler çizmek için.
#bu ilkeller her zaman turtle'ı ilk pozisyonuna döndürür.(yön ve konum olarak)

def direk(t, n):
    """dikey çizgi çeker, ilk po'ya döner."""
    lt(t)
    fdbk(t, n)
    rt(t)

def kiris(t, n, h):
    """verilen yükseklikte yatay çizgi çeker."""#h:yükseklik
    bos(t, n*h)
    fdbk(t, n)
    bos(t, -n*h)

def kolon(t, n, h):
    """verilen yüksekliğe ve yatay çizgiye dikey çizgi çeker ve geri döner."""
    strbas(t, n * h)
    fdbk(t, n)
    lt(t)
    bk(t, n*h)
    rt(t)

def capraz (t, x, y):
    """verilen x,y'de köşegen çizer, geri döner."""
    from math import atan2, sqrt, pi
    a = atan2(y, x) * 180 / pi
    uza = sqrt (x**2 + y**2)
    lt(t, a)
    fdbk(t, uza)
    rt(t, a)

def v(t, n, h):
    capraz(t, -n/2, h*n)
    capraz(t, n/2, h*2)

def yumru(t, n, h):
    """n kadar çap ve h*n kadar yumru yapar"""
    strbas(t, n * h)
    yay(t, n / 2.0, 180)
    lt(t)
    fdlt(t, n * h + n)


"""
harf çizme fonksiyonlarının hepsi önkoşul gerektirir. turtle'ın sol üstte olduğu
ve sonşart gerektirir turtle'ın sağ altta kaldığı.(başladdığı yönde)
urtle'ı ilk argüman, (n)'i 2.argüman olarak alır. Öoğu harf n birim genişlikte
2n birim yüksekliktedir.
"""

def ciz_a(t, n):
    capraz(t, n/2, 2*n)
    kiris(t, n, 1)
    atla(t, n)
    capraz(t, -n/2, 2*n)

def ciz_b(t, n):
    yumru(t, n, 1)
    yumru(t, n, 0)
    atla(t, n/2)

def ciz_c(t, n):
    kolon(t, n, 2)
    fd(t, n)

def ciz_d(t, n):
    yumru(t, 2*n, 0)
    atla(t, n)

def ciz_ef(t, n):
    kolon(t, n, 2)
    kolon(t, n, 1)

def ciz_e(t, n):
    ciz_ef(t, n)
    fd(t, n)

def ciz_f(t, n):
    ciz_ef(t, n)
    atla(t, n)

def ciz_g(t, n):
    kolon(t, n, 2)
    fd(t, n/2)
    kiris(t, n/2, 2)
    fd(t, n/2)
    direk(t, n)

def ciz_h(t, n):
    direk(t, 2*n)
    kolon(t, n, 1)
    atla(t, n)
    direk(t, 2*n)

def ciz_i(t, n):
    kiris(t, n, 2)
    fd(t, n/2)
    direk(t, 2*n)
    fd(t, n/2)

def ciz_j(t, n):
    kiris(t, n, 2)
    yay(t, n/2, 90)
    fd(t, 3*n/2)
    atla(t, -2*n)
    rt(t)
    atla(t, n/2)

def draw_k(t, n):
    direk(t, 2*n)
    strbas(t, n, 180)
    v(t, 2*n, 0.5)
    fdlt(t, n)
    atla(t, n)

def ciz_l(t, n):
    direk(t, 2*n)
    fd(t, n)

def ciz_n(t, n):
    direk(t, 2*n)
    atla(t, n)
    capraz(t, -n, 2*n)
    direk(t, 2*n)

def ciz_m(t, n):
    direk(t, 2*n)
    ciz_v(t, n)
    direk(t, 2*n)

def ciz_o(t, n):
    atla(t, n)
    cember(t, n)
    atla(t, n)

def ciz_p(t, n):
    yumru(t, n, 1)
    atla(t, n/2)

def ciz_q(t, n):
    ciz_o(t, n)
    capraz(t, -n/2, n)

def ciz_r(t, n):
    ciz_p(t, n)
    capraz(t, -n/2, n)

def ciz_s(t, n):
    fd(t, n/2)
    yay(t, n/2, 180)
    yay(t, n/2, -180)
    fdlt(t, n/2, -90)
    atla(t, 2*n)
    lt(t)

def ciz_t(t, n):
    kiris(t, n, 2)
    atla(t, n/2)
    direk(t, 2*n)
    atla(t, n/2)

def ciz_u(t, n):
    direk(t, 2*n)
    fd(t, n)
    direk(t, 2*n)

def ciz_v(t, n):
    atla(t, n/2)
    v(t, n, 2)
    atla(t, n/2)

def ciz_w(t, n):
    ciz_v(t, n)
    ciz_v(t, n)

def ciz_x(t, n):
    capraz(t, n, 2*n)
    atla(t, n)
    capraz(t, -n, 2*n)

def ciz_v(t, n):
    atla(t, n/2)
    capraz(t, -n/2, 2*n)
    capraz(t, n/2, 2*n)
    atla(t, n/2)

def ciz_y(t, n):
    atla(t, n/2)
    strbas(t, n)
    v(t, n, 1)
    rt(t)
    fdlt(t, n)
    atla(t, n/2)

def ciz_z(t, n):
    beam(t, n, 2)
    diagonal(t, n, 2*n)
    fd(t, n)

def ciz_(t, n):
    # boşluk çiz
    atla(t, n)

if __name__ == '__main__':

    # create and position the turtle
    size = 20
    oogway = turtle.Turtle()

    for f in [ciz_u, ciz_n, ciz_i, ciz_v, ciz_e, ciz_r, ciz_s, ciz_e]:
        f(oogway, size)
        atla(oogway, size)

    turtle.mainloop()

