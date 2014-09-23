import os
import imp
import sys
import PyV8 as v8

# set up a global V8 context
ctx = v8.JSContext()
ctx.enter()

class JSImportHook:
	def find_module(self, fullname, path=None):
		name = fullname.split('.')[-1]

		for folder in path or sys.path:
			if os.path.exists(os.path.join(folder, '%s.js' % name)):
				return self

		return None

	def load_module(self, fullname):
		if fullname in sys.modules:
			return sys.modules[fullname]

		sys.modules[fullname] = module = imp.new_module(fullname)

		if '.' in fullname:
			pkg, name = fullname.rsplit('.', 1)
			path = sys.modules[pkg].__path__
		else:
			pkg, name = '', fullname
			path = sys.path

		module.__package__ = pkg
		module.__loader__ = self

		for folder in path:
			if os.path.exists(os.path.join(folder, '%s.js' % name)):
				module.__file__ = os.path.join(folder, '%s.js' % name)
				module.__package__ = pkg
				module.__loader__ = self

				with open(os.path.join(folder, '%s.js' % name)) as f:
					contents = f.read()

				self.eval_module(module, contents)

				return module

		# somehow not found, delete from sys.modules
		del sys.modules[fullname]

	def eval_module(self, module, contents):
		mod = ctx.eval('(function(exports){%s})' % contents)

		mod(module)

# support reload()ing this module
try:
	hook
except NameError:
	pass
else:
	try:
		sys.meta_path.remove(hook)
	except ValueError:
		# not found, skip removing
		pass

# automatically install hook
hook = JSImportHook()

sys.meta_path.insert(0, hook)
