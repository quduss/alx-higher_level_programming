#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted linked list
 * @head: pointer to pointer to head node of list
 * @number: number to be inserted
 * Return: pointer to new node or null if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *ptr;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if ((*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	ptr = *head;
	while (ptr)
	{
		if (ptr->next->n >= number)
		{
			new_node->next = ptr->next;
			ptr->next = new_node;
			return (new_node);
		}
		if (ptr->next == NULL)
		{
			ptr->next = new_node;
			return (new_node);
		}
		ptr = ptr->next;
	}
	free(new_node);
	return (NULL);
}
