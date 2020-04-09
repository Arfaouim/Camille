class complex(object):
	"""docstring for complex"""
	version="0.12"
	def __init__(self, realpart, imagpart):
		super(complex, self).__init__()
		self.re = realpart
		self.im = imagpart
	def algebric_forme(self):
		"""
		A complex number z is generally presented in algebraic form as a sum a + ib,
	    where a and b are arbitrary real numbers and where i is a particular number 
	    such that i ** 2 = –1. The real a is called the real part of z and is noted 
	    Re (z), the real b is its imaginary part and is noted Im (z)
		"""
	    return print("{}+i{}".format(self.re,self.im))  	
	#def exponential_form (self):
	   
		
x=complex(1,1)	
x.algebric_forme()
print(complex.__doc__)	
	
