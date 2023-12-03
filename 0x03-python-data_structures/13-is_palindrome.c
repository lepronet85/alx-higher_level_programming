#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head, *fast = *head;
	listint_t *second_half, *prev_of_slow = *head;
	listint_t *mid_node = NULL;
	int is_palindrome = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		prev_of_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	second_half = slow;
	prev_of_slow->next = NULL;
	reverse_list(&second_half);

	is_palindrome = compare_lists(*head, second_half);

	reverse_list(&second_half);

	if (mid_node != NULL)
	{
		prev_of_slow->next = mid_node;
		mid_node->next = second_half;
	}
	else
		prev_of_slow->next = second_half;

	return (is_palindrome);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 */

void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the first linked list
 * @list2: pointer to the second linked list
 * Return: 1 if lists are identical, 0 otherwise
 */

int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	if (list1 == NULL && list2 == NULL)
		return (1);

	return (0);
}
