# Copyright (c) 2013, WayzonTech and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Bank')

class TestBank(unittest.TestCase):
	pass
