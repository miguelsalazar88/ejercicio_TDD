from funcion import menor

def test_menor():
    assert menor([1,2,3,4,5]) == 1
    assert menor([9,8,7,6,5]) == 5
    assert menor([78, 84, 6, 96, 6]) == 6
    assert menor([92, 32, 35, 21, 8]) == 8
    assert menor([49, 44, 85, 87, 90]) == 44
    assert menor([59, 62, 58, 48, 41]) == 41
    assert menor([85, 2, 44, 46, 26]) == 2
    assert menor([18, 3, 13, 48, 89]) == 3
    assert menor([65, 40, 70, 78, 96]) == 40
    assert menor([6, 74, 3, 73, 57]) == 3
    assert menor([88, 6, 26, 91, 75]) == 6
    assert menor([19, 20, 4, 16, 71]) == 4