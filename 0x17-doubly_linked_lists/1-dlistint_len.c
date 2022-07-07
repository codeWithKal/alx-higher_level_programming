#include "lists.h"
/**
 * dlistint_len - computes the total number of elements in nodes
 * @h: pointer to the head of a list
 * Return: the number of elements
 */
size_t dlistint_len(const dlistint_t *h)
{
	int elements = 0;

	while (h != NULL)
	{
		elements++;
		h = h->next;
	}
	return (elements);
}
