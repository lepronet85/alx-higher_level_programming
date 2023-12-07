#include <Python.h>

void print_info_list(PyObject *p);
void print_info_bytes(PyObject *p);

/**
 * print_info_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_info_list(PyObject *p)
{
    Py_ssize_t size;
    Py_ssize_t alloc;
    Py_ssize_t i;
    const char *type;
    PyListObject *list = (PyListObject *)p;

    size = PyList_Size(list);
    alloc = PyList_GET_ALLOC(list);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", alloc);

    for (i = 0; i < size; i++)
    {
        type = Py_TYPE(list->ob_item[i])->tp_name;
        printf("Element %zd: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
        {
            print_info_bytes(list->ob_item[i]);
        }
    }
}

/**
 * print_info_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_info_bytes(PyObject *p)
{
    Py_ssize_t i, size;
    PyBytesObject *bytes = (PyBytesObject *)p;

    if (!PyBytes_CheckExact(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(bytes);
    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(bytes));

    if (size > 10)
        size = 10;
    else
        size = ((PyVarObject *)p)->ob_size + 1;

    printf("  first %zd bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx", PyBytes_AS_STRING(bytes)[i]);
        if (i == (size - 1))
            printf("\n");
        else
            printf(" ");
    }
}
