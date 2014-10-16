all: graficafinal.jpg plots.py Solucion.dat

graficafinal.jpg:	plots.py
	python plots.py
plots.py:	Solucion.dat
	python plots.py
Solucion.dat:	pendulum.py
	python pendulum.py
