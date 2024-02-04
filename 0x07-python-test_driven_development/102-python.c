#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Prints Python strings.
 * @p: A pointer to a PyObject.
 * Return: Nothing
 */
void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  type: %s\n", Py_TYPE(p)->tp_name);
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
	}
	else
	{
		fprintf(stderr, "[.] Invalid String Object\n");
	}
}

