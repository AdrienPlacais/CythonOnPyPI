clean:
	rm -rf build dist cython_on_pypi.egg-info

clean-ext:
	rm -f src/cython_on_pypi/converters/*.{c,so}

compile:
	python setup.py build_ext --inplace
