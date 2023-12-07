#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t alloc = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *typeName = item->ob_type->tp_name;
        printf("Element %ld: %s\n", i, typeName);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *data = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  [.] size: %ld\n", size);
    printf("  [.] trying string: %s\n", data ? data : "(no data)");

    printf("  [.] first 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; i++) {
        printf("%02hhx ", data[i]);
    }
    printf("\n");
}
