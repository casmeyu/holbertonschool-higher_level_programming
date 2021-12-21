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
	listint_t *tortuga = list, *liebre = list;

	if (!list)
		return (0);

	while (liebre->next != NULL && liebre->next->next != NULL)
	{
		liebre = liebre->next->next;
		tortuga = tortuga->next;

		if (liebre == tortuga) /* liebre catched up */
			return (1);
	}
	return (0);
}
