#include <Python.h>

void print_info_python_list(PyObject *p);
void print_info_python_bytes(PyObject *p);

/**
 * print_info_python_list - Display basic information about Python lists.
 * @p: A PyObject list object.
 */
void print_info_python_list(PyObject *p)
{
    int list_size, list_allocated, index;
    const char *element_type;
    PyListObject *list_obj = (PyListObject *)p;
    PyVarObject *var_obj = (PyVarObject *)p;

    list_size = var_obj->ob_size;
    list_allocated = list_obj->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", list_size);
    printf("[*] Allocated = %d\n", list_allocated);

    for (index = 0; index < list_size; index++)
    {
        element_type = list_obj->ob_item[index]->ob_type->tp_name;
        printf("Element %d: %s\n", index, element_type);
        if (strcmp(element_type, "bytes") == 0)
            print_info_python_bytes(list_obj->ob_item[index]);
    }
}

/**
 * print_info_python_bytes - Display basic information about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_info_python_bytes(PyObject *p)
{
    unsigned char byte_index, byte_size;
    PyBytesObject *bytes_obj = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf("  trying string: %s\n", bytes_obj->ob_sval);

    if (((PyVarObject *)p)->ob_size > 10)
        byte_size = 10;
    else
        byte_size = ((PyVarObject *)p)->ob_size + 1;

    printf("  first %d bytes: ", byte_size);
    for (byte_index = 0; byte_index < byte_size; byte_index++)
    {
        printf("%02hhx", bytes_obj->ob_sval[byte_index]);
        if (byte_index == (byte_size - 1))
            printf("\n");
        else
            printf(" ");
    }
}

