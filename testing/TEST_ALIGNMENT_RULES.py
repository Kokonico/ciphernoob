## ! TEST ALIGNMENT RULES ! ##

import unittest

## ! spacing must match all the requirments ! ##


### ! VVV | STARTING HERE | VVV ! ###



# class name

class exampletest(unittest.TestCase):

  
  # test name

  def sample_test(self):
    # 0 - 2 lines, what looks best.
    
    
    # mini test desc
    self.assertEqual("first", "second")
    # IF ONE LINE:
    # no space
    self.assertEqual("first", "second")
    self.assertEqual("first", "second")
    # ELSE:
    # 1 or 2 lines between depending on how it looks. 
    # longer multi-line mini-tests should have two lines between.
    self.assertEqual(
      "first",
      "second"
    )

    self.assertEqual(
      "first",
      "second"
    )
  # THREE LINES between each test. 2 lines above name, one below. 
  # (name on it's own line).
  

  # test name 2

  def test_2(self):
    self.assertEqual("first", "second")
    self.assertEqual("first", "second")
# FIVE LINES before next class. four above class name, one below. (class name has own line)




# another class name

class extest2(unittest.TestCase):

  def sample_test_2(self):
    self.assertEqual("first", "second")
    self.assertEqual("first", "second")


# example, no commentary.

## VVV VVV ###

class exampletest2(unittest.TestCase):

  
  # test name

  def sample_test(self):
    
    self.assertEqual("first", "second")
    self.assertEqual("first", "second")
    
    self.assertEqual(
      "first",
      "second"
    )

    self.assertEqual(
      "first",
      "second"
    )
  

  # test name 2

  def test_2(self):
    self.assertEqual("first", "second")
    self.assertEqual("first", "second")




# another class name

class extest3(unittest.TestCase):

  def sample_test_2(self):
    self.assertEqual("first", "second")
    self.assertEqual("first", "second")