#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a node into an ordered single linked list
 *
 * @head: head node of the list
 * @number: value for the new node
 * Return: the linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	int flag = 0;
	listint_t *new, *prev, *current, *next;

	if (!head)
		return (NULL);

	new = malloc(sizeof(*new));
	if (!new)
		return (*head);

	prev = *head;
	current = *head;
	next = current->next;
	new->n = number;
	while (next)
	{
		if (number <= current->n)
		{
			new->next = next;
			if (prev == current)
			{
				*head = new;
				new->next = prev;
			}
			else
				prev->next = new;
			return (*head);
		}
		else
		{
			if (flag == 1)
				prev = prev->next;
			current = current->next;
			next = next->next;
			flag = 1;
		}
	}
	current->next = new;
	return (*head);
}
