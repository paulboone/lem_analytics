
from pylem import calc_drainage_area

def test_calc_drainage_area_w_line_should_be_02020():
    assert list(calc_drainage_area([1,0,1,0,1], 1.0)) == [0.0,2.0,0.0,2.0,0.0]

def test_calc_drainage_area_m_line_should_be_10201():
    assert list(calc_drainage_area([0,1,0,1,0], 1.0)) == [1.0,0.0,2.0,0.0,1.0]

def test_calc_drainage_area_deep_w_line_should_be_0126210126210():
    assert list(calc_drainage_area([3,2,1,0,1,2,3,2,1,0,1,2,3], 1.0)) == [0,1,2,6,2,1,0,1,2,6,2,1,0]

def test_calc_drainage_area_deep_m_line_should_be_3210126210123():
    assert list(calc_drainage_area([0,1,2,3,2,1,0,1,2,3,2,1,0], 1.0)) == [3,2,1,0,1,2,6,2,1,0,1,2,3]

def test_calc_drainage_area_x_size_halved_should_halve_drainage_area():
    z = [10,8,4,2,1]
    assert list(calc_drainage_area(z, 2)) == [0,2,4,6,8]
    assert list(calc_drainage_area(z, 1)) == [0,1,2,3,4]
