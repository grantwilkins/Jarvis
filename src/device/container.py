class Container(object):
	"""docstring for Container"""
	def __init__(self, ingredient_name, container_level, container_num):
		super(Container, self).__init__()
		self.ingredient_name = ingredient_name
		self.container_level = container_level
		self.container_num = container_num

	def decrease_level(self, amount):
		self.container_level -= amount

	def update_drink(self, new_name, new_amount):
		self.ingredient_name = new_name
		self.container_level = new_amount

	def get_ingredient_name(self):
		return self.ingredient_name
	
	def get_container_level(self):
		return self.container_level
	
	def get_container_num(self):
		return self.container_num
	
	def set_container_level(self, new_level):
		self.container_level = new_level
	
	def set_ingredient_name(self, new_name):	
		self.ingredient_name = new_name