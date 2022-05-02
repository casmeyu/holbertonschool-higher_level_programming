#include "search_algos.h"
#include <stdio.h>
/**
 * binary_search - searchs for an item of a given value using binary search
 *
 * @array: array of items to search in
 * @size: size of the array
 * @value: value to search for
 *
 * Return: index of the value found or -1 if it doesnt exists
 */
int binary_search(int *array, size_t size, int value)
{
	size_t idx;

	if (size < 1 || !value || !array)
		return (-1);

	printf("Searching in array: ");
	for (idx = 0; idx < size; idx++)
	{
		if (idx != 0)
			printf(", ");
		printf("%d ", array[idx]);
	}
	printf("\n");
	idx = ((size - 1) / 2);
	if (array[idx] == value)
		return (idx);

	if (value < array[idx])
		return (binary_search(array, idx, value));
	else
		return (binary_search(&array[idx + 1], (size - idx - 1), value));

	return (-1);
}
