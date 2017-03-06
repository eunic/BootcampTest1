import unittest
import solution

class TestSoution(unittest.TestCase):

	def test_addition(self):
		self.assertTrue(solution.solution(10,20,"+"),30)
		#self.assertTrue(solution(20,10,"-"),10)
		#self.assertTrue(solution(20,10,"/"),10)
		#self.assertTrue(solution(20,10,"*"),10)

if __name__ == "__main__":
	unittest.main()