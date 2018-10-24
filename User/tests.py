from django.test import TestCase

# Create your tests here.
from CommonUtils.imgUtils import imgUtil

class TestUser(TestCase):
    def testVertify(self):
        code = imgUtil(None, None).get_vertify_img()
        print(code)


if __name__ == '__main__':
    tu = TestUser
    tu.testVertify(tu)
