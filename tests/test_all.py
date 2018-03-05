#!/usr/bin/env python
import numpy as np
from pyiri2016 import IRI2016

def test_main1():

    Obj = IRI2016()
    IRIData, IRIDATAAdd = Obj.IRI('1980-03-21T12', 130., 0., 0., 5, 150, 150, 1)

    np.testing.assert_allclose((IRIData['ne'], IRIDATAAdd['NmF2'], IRIDATAAdd['hmF2']),
                    (267285184512.0, 2580958937088.0, 438.78643798828125))


if __name__ == '__main__':
    np.testing.run_module_suite()
