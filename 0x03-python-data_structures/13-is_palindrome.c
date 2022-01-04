#include "lists.h"
/**
 * reverse_listint - reverse a singly linked list
 * @head: pointer to the linked list
 *
 * Return: number of nodes in the list
 */
listint_t *reverse_listint(listint_t **head)
{
	unsigned int len = 0;
	listint_t *prev = NULL, *current = NULL, *next = NULL;

	if (head == NULL)
		exit(98);

	current = (*head);

	while (current)
	{
		next = current->next;

		current->next = prev;

		prev = current;

		current = next;

		len++;
	}

	(*head) = prev;

	return (*head);
}

/**
 * is_palindrome - checks if a linked list is a palindrome list
 *
 * @head: head node of list to check
 * Return: 1 if it is palindorme | 0 if not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *origin = *head, *rev = *head;

	if (!head)
		return (1);

	reverse_listint(&rev);

	while (origin->next)
	{
		if (origin->n != rev->n)
			return (0);

		origin = origin->next;
		rev = rev->next;
	}
	return (1);
}
