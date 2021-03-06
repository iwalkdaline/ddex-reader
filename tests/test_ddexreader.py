#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import pytest

from ddexreader.ddexreader import open_ddex, ddex_to_dict


@pytest.fixture(scope='session', params=[ '382'])

def xml_file(request):
    return os.path.abspath(os.path.join('fixtures', 'ern', request.param, 'instance1.xml'))


def test_parse_ddex(xml_file):
    # Check that we can successfully parse the DDEX files under ern37
    # if '37' not in xml_file:
    ddex = open_ddex(xml_file)
    ddex_to_dict(ddex)
    # else:
        # # Else raise a ValueError
        # with pytest.raises(ValueError):
        #     open_ddex(xml_file)
