#include "lists.h"
#include <stdlib.h>
/**
 * compareLists - compares the data of the first half and second half of the list
 * @head_1: first half of linked list
 * @head_2: second half of linked list
 * Return: 0 if it is not palindrome, 1 if it is palindrome
 */
int compareLists(listint_t *head_1, listint_t *head_2)
{
	while (head_1 && head_2)
	{
		if (head_1->n == head_2->n)
		{
			head_1 = head_1->next;
			head_2 = head_2->next;
		}
		else
			return (0);
	}
	if (head_1 == NULL && head_2 == NULL)
		return (1);
	else
		return (0);
}

/**
 * reverse - reverses a linked list
 * @head_ref: pointer to pointer to head node of the reversed list
 */
void reverse(listint_t **head_ref)
{
	listint_t *current = *head_ref, *next, *prev = NULL;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_ref = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head node of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast_ptr = *head, *slow_ptr = *head, *mid_node = NULL, *prev_of_slow_ptr, *second_half;
	int result;

	if (*head == NULL)
		return (1);
	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			prev_of_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		if (fast_ptr != NULL)
		{
			mid_node = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		second_half = slow_ptr;
		prev_of_slow_ptr->next = NULL;
		reverse(&second_half);
		result = compareLists(*head, second_half);
		reverse(&second_half);
		if (mid_node != NULL)
		{
			prev_of_slow_ptr->next = mid_node;
			mid_node->next = second_half;
		}
		else
			prev_of_slow_ptr->next = second_half;
		return (result);
	}
	return (0);
}
