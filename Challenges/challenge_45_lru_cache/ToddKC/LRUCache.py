class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.memory = {}
		self.usage = []

	def get(self, key):
		try:
			#print if found
			print(self.memory[key])
			#remove from usage list
			if key in self.usage: self.usage.remove(key)
			#add to end of usage list
			self.usage.append(key)
		except:
			# print -1 if not found
			print(-1)

	def put(self, key, value):
		#assign k/v to memory
		self.memory[key] = value
		#remove from usage list
		if key in self.usage: self.usage.remove(key)
		#add to end of usage list
		self.usage.append(key)
		#if over capacity remove last used item
		if len(self.memory) > self.capacity:
			self.memory.pop(self.usage[0])
			self.usage.pop(0)
