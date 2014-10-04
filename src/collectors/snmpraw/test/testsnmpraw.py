#!/usr/bin/python
# coding=utf-8
###############################################################################

from test import CollectorTestCase
from test import get_collector_config
from test import unittest

from snmpraw import SNMPRawCollector


###############################################################################

class TestSNMPRawCollector(CollectorTestCase):
    def setUp(self):
        config = get_collector_config('SNMPRawCollector', {
        })
        self.collector = SNMPRawCollector(config, None)

    def test_import(self):
        self.assertTrue(SNMPRawCollector)

###############################################################################
if __name__ == "__main__":
    unittest.main()
