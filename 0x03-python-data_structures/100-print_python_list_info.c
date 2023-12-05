#include <Python.h>

void print_python_list_info(PyObject *p) {
    Py_ssize_t size, allocated, i;
    PyListObject *list = (PyListObject *)p;

    size = PyList_Size(p);
    allocated = list->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++) {
        printf("Element %zd: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
    }
}

