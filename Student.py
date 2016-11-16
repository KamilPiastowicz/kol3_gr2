class Student(object):
	def __init__(self,name,surname,scores,attendances):
		self.name = name
		self.surname = surname
		self.scores = scores
		self.attendances = attendances
		

	def get_name(self):
		return self.name

	def get_surname(self):
		return self.surname

	def show_student(self):
		return self.get_name() +  self.get_name()

	def get_scores(self):
	        return sum(self.scores)

	def get_attendances(self):
		return sum(self.attendances)
	
	def avg_total(self):
		return sum(self.scores)/len(self.scores)
	
	def avg_subject(self):
		pass
