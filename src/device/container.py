class Container(object):
	"""docstring for Container"""
	def __init__(self, drink_name, container_level, container_num):
		super(Container, self).__init__()
		self.drink_name = drink_name
		self.container_level = container_level
		self.container_num = container_num

	def decrease_level(self, amount):
		self.container_level -= amount

	def update_drink(self, new_name, new_amount):
		self.drink_name = new_name
		self.container_level = new_amount