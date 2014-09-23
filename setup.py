from setuptools import setup, find_packages

setup(
	name='jsmod',
	version='0.0.1',
	description='',
	url='https://github.com/sciyoshi/jsmod/',
	author='Samuel Cormier-Iijima',
	author_email='sciyoshi@gmail.com',
	license='MIT',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
	],
	keywords='pyv8 javascript jsmod import importhooks hook',
	install_requires=[
		'pyv8>=1.0-dev'
	],
	py_modules=[
		'jsmod'
	])
