from sympy import Matrix
from sympy.abc import x, y, z
from numpy import array
from numpy.testing import assert_array_equal

from lmi_sdp import LMI_PSD, LMI_NSD
from lmi_sdp import prepare_lmi_for_sdp, prepare_objective_for_sdp


def test_prepare_lmi_for_sdp():
    vars = [x, y, z]
    m1 = Matrix([[x, y], [y, z+1]])
    c1 = Matrix([[0, 1], [1, 2]])
    lmi1 = LMI_PSD(m1, c1)
    m2 = Matrix([[y, 0], [0, 2*x]])
    c2 = Matrix([[30, 0], [0, 40]])
    lmi2 = LMI_NSD(m2, c2)
    coeffs = prepare_lmi_for_sdp([lmi1, lmi2], vars,
                                 optimize_by_diag_blocks=True)
    expected = [([array([[1., 0.],
                         [0., 0.]]),
                  array([[0., 1.],
                         [1., 0.]]),
                  array([[0., 0.],
                         [0., 1.]])],
                 array([[0., -1.],
                        [-1., -1.]])),
                ([array([[0.]]),
                  array([[-1.]]),
                  array([[0.]])],
                 array([[30.]])),
                ([array([[-2.]]),
                  array([[0.]]),
                  array([[0.]])],
                 array([[40.]]))]
    for i in range(len(coeffs)):
        assert_array_equal(coeffs[i][0], expected[i][0])
        assert_array_equal(coeffs[i][1], expected[i][1])


def test_prepare_objective_for_sdp():
    vars = [x, y, z]
    assert_array_equal(prepare_objective_for_sdp(1.2 + x - 3.4*y, vars, 'max'),
        array([-1.0, 3.4, 0.0]))

    except_ok = False
    try:
        prepare_objective_for_sdp(1.2 + x*y, vars)
    except ValueError:
        except_ok = True
    assert except_ok
