#coding:utf-8


import __builtin__

try:
    profile = __builtin__.__dict__['profile']
except KeyError:
    # No line profiler, provide a pass-through version
    def profile(func): return func
    __builtin__.profile = profile

class Word:
	"""词语
	Attributes:
		freq： 频率
		pmi: 凝固度
		free：自由度		
	"""
	
	__slots__ = ["text",'left','right','freq','pmi','entropy']
	def __init__(self, text):
		self.text = text
		self.left = {}
		self.right = {}
		self.freq = 0
		self.pmi = None
		self.entropy = None

	def incr(self):
		self.freq = self.freq + 1

	def get_freq(self):
		"""频率"""
		return self.freq
	
	def add_left(self, zi):
		self.left[zi] = self.left.get(zi,0) + 1

	def add_right(self, zi):
		self.right[zi] = self.right.get(zi,0) + 1
	
	def toString(self):
		return "%5s\tFRQ:%4s\tSOL:%.2f\tENT:%.2f" % (self.text,self.freq,self.pmi, self.entropy)
