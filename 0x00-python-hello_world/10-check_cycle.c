#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle or not
 * @list: pointer to the head of the list
 * Return: 0 if no cycle, 1 if there's a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_p, *fast_p;

	slow_p = list;
	fast_p = list;
	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
			return (1);
	}
	return (0);
}
