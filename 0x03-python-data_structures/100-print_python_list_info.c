#include "Python.h"
#include <stdlib.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *list = NULL;
	ssize_t idx, length = 0;
	const char *item_type = NULL;

	list = (PyListObject *)p;
	length = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %ld\n", (list->allocated));

	for (idx = 0; idx < length; idx++)
	{
		item_type = Py_TYPE(list->ob_item[idx])->tp_name;
		printf("Element %ld: %s\n", idx, item_type);
	}

}
