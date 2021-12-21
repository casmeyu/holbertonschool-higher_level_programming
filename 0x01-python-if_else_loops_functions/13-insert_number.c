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
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!*head)
		*head = new, return (*head);
	prev = *head;
	current = *head;
	next = current->next;
	while (next)
		if (number < current->n)
		{
			new->next = next;
			if (flag == 0)
				new->next = prev, *head = new;
			else
				prev->next = new, new->next = current;
			return (new);
		}
		else
		{
			if (flag == 1)
				prev = prev->next;
			current = current->next;
			next = next->next;
			flag = 1;
		}
	current->next = new;
	return (new);
}
