==============================
Use 7-base_geometry module
==============================

>>> BaseGeometry = __import__('7-base_geometry').BaseGeometry

::
    >>> base1 = BaseGeometry()
    >>> base1.area()
    Traceback (most recent call last):
    Exception: area() is not implemented

::

    >>> base2 = BaseGeometry()
    >>> base2.integer_validator("name", -5)
    Traceback (most recent call last):
    ValueError: name must be greater than 0

::

    >>> base3 = BaseGeometry()
    >>> base3.integer_validator("name", 0)
    Traceback (most recent call last):
    ValueError: name must be greater than 0

::

    >>> base4 = BaseGeometry()
    >>> base4.integer_validator("name", 7)

::

    >>> base5 = BaseGeometry()
    >>> base5.integer_validator("name")
    Traceback (most recent call last):
    TypeError: integer_validator() missing 1 required positional argument: 'value'

::

    >>> base6 = BaseGeometry()
    >>> base6.integer_validator("name", 8, 4)
    Traceback (most recent call last):
    TypeError: integer_validator() takes 3 positional arguments but 4 were given

::

    >>> base7 = BaseGeometry()
    >>> base7.integer_validator("name", "2")
    Traceback (most recent call last):
    TypeError: name must be an integer

::

    >>> base8 = BaseGeometry()
    >>> base8.integer_validator("age", {5, 12})
    Traceback (most recent call last):
    TypeError: age must be an integer
