import unittest

class ImportModule(unittest.TestCase):

    def test_import(self):
        try:
            import cleware
        except Exception as e:
            print(e)
            self.fail("unable to import the cleware module")

    def test_instantiate(self):
        try:
            import cleware
            c = cleware.CUSBaccess()        
        except Exception as e:
            print(e)
            self.fail("unable to instantiate a cleware access object")

    def test_enumerate(self):
        try:
            import cleware
            c = cleware.CUSBaccess()
            n_devices = c.OpenCleware()
        except Exception as e:
            print (e)
            self.fail("unable to enumerate the cleware devices")
