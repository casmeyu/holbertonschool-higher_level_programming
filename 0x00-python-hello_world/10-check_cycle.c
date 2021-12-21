#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if there is a cycle in a single linked list of integers
 *
 * @list: sinlge linked list
 * Return: 1 if has cycle | 0 if not cycle
 */

int check_cycle(listint_t *list)
{
	int i = 0, j = 0;
	listint_t *past_node[1024];

	if (!list)
		return (0);

	while (list && i < 10)
	{
		past_node[i] = list;
		i++;
		for (j = 0; past_node[j]; j++)
		{
			if (list->next == past_node[j])
				return (1);
		}
		list = list->next;
	}
	return (0);
}
