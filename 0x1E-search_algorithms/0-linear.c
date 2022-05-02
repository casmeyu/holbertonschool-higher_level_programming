#include "search_algos.h"
#include <stddef.h>
#include <stdio.h>
/**
 * linear_search - searchs for a value in an array of ints in O(n)
 *
 * @array: array to search in
 * @size: size of the array
 * @value: value to search for
 * Return: value found or -1 if doesnt exists
 */
int linear_search(int *array, size_t size, int value)
{
	size_t idx;

	if (size < 1 || !value || !array)
		return (-1);
	for (idx = 0; idx < size; idx++)
	{
		printf("Value checked array[%ld] = [%d]\n", idx, array[idx]);
		if (array[idx] == value)
			return (value);
	}
	return (-1);
}
