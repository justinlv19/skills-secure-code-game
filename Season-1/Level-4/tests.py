'''
Please note:

The first file that you should run in this level is tests.py for database creation, with all tests passing.
Remember that running the hack.py will change the state of the database, causing some tests inside tests.py
to fail.

If you like to return to the initial state of the database, please delete the database (level-4.db) and run 
the tests.py again to recreate it.
'''

import unittest
import code as c

class TestDatabase(unittest.TestCase): 
  
    # tests for correct retrieval of stock info given a symbol
    def test_1(self):
        op = c.DB_CRUD_ops()
        expected_output = "[METHOD EXECUTED] get_stock_info\n[QUERY] SELECT * FROM stocks WHERE symbol = 'MSFT'\n[RESULT] ('2022-01-06', 'MSFT', 300.0)"
        actual_output = op.get_stock_info('MSFT')
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':    
    unittest.main()