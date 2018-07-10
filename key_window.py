import ctypes
class key_dict_windows():
	keys={"copy":(0,1,0x0002,0x5a)}
	def __init__(self):
		pass
	@staticmethod
	def call(func,*args):
		func(args)
	@staticmethod
	def block(param):
		try:
			key_dict_windows.call(ctypes.windll.user32.RegisterHotKey,key_dict_windows.keys.get(param))
		except Exception as e:
			print("\n\n")
			print(e)
			pass

  

"""cut copy past undo
			print screen 
			alt tab
			windows
			
"""			