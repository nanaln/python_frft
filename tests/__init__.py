import frft
import numpy


def precision(a):
    """
    Test if transform-inverse identity holds

    """
    siglen = 2048

    i = numpy.random.random(siglen)
    x = frft.frft(i, a)
    y = frft.ifrft(x, a)

    assert numpy.allclose(i, y)


def test_precision():
    for a in range(40):
        yield precision, a / 10.0
