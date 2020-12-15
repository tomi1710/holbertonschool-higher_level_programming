#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	PyObject* repr = p;
	PyObject* str = PyUnicode_AsEncodedString(repr, "utf-8", "~E~");
	const char *bytes = PyBytes_AS_STRING(str);

	printf("REPR: %s\n", bytes);

	Py_XDECREF(repr);
	Py_XDECREF(str);
}
