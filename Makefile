extension = vix/_vixc.so

all: $(extension)

$(extension): 
	python setup.py build_ext --inplace

clean:
	rm -f *.o *.so vix_wrap.c vix.py *.pyc

test: $(extension)
	nosetests

.PHONY: $(extension)

