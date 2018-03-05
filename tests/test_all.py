#!/usr/bin/env python
import numpy as np
from pyiri2016 import IRI2016

def test_main1():

    iri = IRI2016().IRI('1980-03-21T12', 130., 0., 0.)

    np.testing.assert_allclose((iri.loc[:,'ne'].item(), iri.attrs['NmF2'], iri.attrs['hmF2']),
                    (267285184512.0, 2580958937088.0, 438.78643798828125))

    print('assert passed')


if __name__ == '__main__':
    np.testing.run_module_suite()
