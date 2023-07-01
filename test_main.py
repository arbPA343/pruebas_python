import pytest
from main import multi, es_menor_que, login

#Test de pruebas que pasan

def test_multi():
    assert multi(40,5) == 200
    print("La función multi1 trabaja correctamente")
    
def test_menor():
    assert es_menor_que(4,52)
    print("La función menor1 trabaja correctamente")
    
def test_multi2():
    assert multi(3,5) == 15
    print("La función suma2 trabaja correctamente")
    
def test_menor2():
    assert es_menor_que(1,24)
    print("La función menor2 trabaja correctamente")
    
def test_login_pass():
    login_passes = login("Univalle", "890399010-6")
    assert login_passes

#Test de pruebas que fallan

def test_multi3():
    assert multi(40,5) == 100
    print("La función multi1 trabaja correctamente")
    
def test_menor3():
    assert es_menor_que(52,4)
    print("La función menor1 trabaja correctamente")
    
def test_multi4():
    assert multi(3,5) == 51
    print("La función suma2 trabaja correctamente")
    
def test_menor4():
    assert es_menor_que(8,4)
    print("La función menor2 trabaja correctamente")
    
def test_login_fail():
    login_passes = login("Univalle", "890399011-6")
    assert login_passes
    
@pytest.mark.parametrize(
    "input_x, input_y, esperado",
    [
        (3, 4, 12),
        (multi(3,1), multi(2,2), 12),
        (3, 5, multi(4,2)),
    ]
)
def test_multi_params(input_x, input_y, esperado):
    assert multi(input_x, input_y) == esperado
    print("Las funciones parametrizadas trabajan correctamente")
    
def test_login_fail():
    login_fails = login("Metodologias", "710012C")
    assert not login_fails

if __name__ == '__main__':
    test_multi()
    test_menor()
    test_multi2()
    test_menor2()
    test_multi3()
    test_menor3()
    test_multi4()
    test_menor4()
 