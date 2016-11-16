import unittest
from Student import Student

#TestModule testing implementation of Student class by pgruszczynski93

class test_class_student(unittest.TestCase):
 def setUp(self):
  self.stud = Student("name","surname",[2,2,2,2],[1,0,0,1])

 def test_get_name_returns_student_name(self):
  self.assertEqual("name",self.stud.get_name())
 
 def test_get_surname_returns_student_surname(self):
  self.assertEqual("surname",self.stud.get_name()) 

 def test_show_student_returns_student_name_surname(self):
  self.assertEqual("name surname",self.stud.show_student())

 def test_get_scores_returns_sum_score(self):
  self.assertEqual(8,self.stud.get_scores())

 def test_get_attendances_return_sum_attendances(self):
  self.assertEqual(2,self.stud.get_attendances())

 def test_avg_total_returns_average_mark(self):
  self.assertEqual(2,self.stud.avg_total())

if __name__ == "__main__":
 unittest.main()
