#include "lists.h"
/**
 * print_dlistint - prints all elements of a list
 * @h: a pointer to the head of a list
 * Return: the number of list
 */

size_t print_dlistint(const dlistint_t *h)
{
	int nodes = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
			nodes++;
		h = h->next;
	}
	return (nodes);
}
