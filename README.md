# Primeros pasos con Python: Manipulando imágenes 🖼⟷💻

> **Author:** Rodolfo Ferro Pérez <br/>
> **Email:** [ferro@cimat.mx](mailto:ferro@cimat.mx) <br/>
> **Twitter:** [@FerroRodolfo](http://twitter.com/FerroRodolfo) <br/>

## About 🕹

This is a Python 🐍 workshop for the *Festival Latinoamericano de Instalación de Software Libre 2017 ([FLISoL](https://flisol.info/FLISOL2017/Mexico/Leon))* for which I was invited at the *Instituto Tecnológico de León*. It is basically a workshop about some Python basics, focused on image manipulation.

I don't use any lib other than NumPy and Matplotlib to manipulate images, since I was asked to teach through the basics. Even tho, I coded some image derivatives (sobel X and sobel Y) to illustrate some image processing, and coded some fractals.


## Setup ⚙️

You can download Python from the [official site](https://www.python.org/downloads/). For this workshop, version 3.6 is recommended (we will be using operators such as `@`). We will also need to install [NumPy](http://numpy.org) and [Matplotlib](http://matplotlib.org).

> If you're installing Python on Windows, just remember to check the "Add Python to PATH" little box during the installation.

#### Installing NumPy and Matplotlib:

To install `numpy` and `matplotlib` we will use `pip`. After installing Python, open a terminal and enter the following:
```
$ pip install numpy
```

Now enter the following:
```
$ pip install matplotlib
```

> If you want not only to install this libs on your user, but in the whole system, use `sudo`.

#### Checking your installation:

To check if the installation was successful, on the open terminal open your Python prompt by entering:
```
$ python
```
Something like this should have appeared in your console:
![Python prompt](https://github.com/RodolfoFerro/FLISoL17/blob/master/imgs/prompt.png "Python prompt")

Now try to import `numpy` and `matplotlib` as follows:
```
>>> import numpy
>>> import matplotlib
```
If any error is raised, congrats! Now you're all set to go.

## Content 👾

* You can find the lecture [here](https://github.com/RodolfoFerro/FLISoL17/tree/master/python.pdf).
* You can find the scripts folder [here](https://github.com/RodolfoFerro/FLISoL17/tree/master/scripts).
* You can find some images [here](https://github.com/RodolfoFerro/FLISoL17/tree/master/imgs).

***

### ABOUT COPYING OR USING PARTIAL INFORMATION: 🔐
> These documents were originally created by the author.
> Any usage of these documents or their contents is granted according to the provided license and its conditions.
> For any question, you can contact the author via email or Twitter.


#### Want to see an awesome fractal? Check this one:
![Built from Mandelbrot set using Python](https://github.com/RodolfoFerro/FLISoL17/blob/master/imgs/mandel.png "Built from Mandelbrot set using Python")

**Copyright (c) 2017 Rodolfo Ferro**
