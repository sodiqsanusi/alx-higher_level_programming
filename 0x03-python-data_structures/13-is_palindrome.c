#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* add_node - Adds a new node at the beginning of a singly-linked list
* @head: A pointer to a pointer that points to the first node
* @n: The number stored i the new node
*
* Return: "list_t"  A pointer to the newly created list
*/
listint_t *add_node(listint_t **head, const int n)
{
	nodePtr currentNode = *head;
	nodePtr newNode = malloc(sizeof(listint_t));

	if (newNode == NULL)
		return (NULL);

	newNode->n = n;
	newNode->next = NULL;

	if (!head)
		return (newNode);
	if (*head == NULL)
		*head = newNode;
	else
	{
		newNode->next = currentNode;
		*head = newNode;
	}

	return (*head);
}

/**
 * is_palindrome - Checks if a singly-linked list is a palindrome
 * @head: "listint_t **" A pointer to the first pointer of the head node
 *
 * Return: "int" 1 if list is a palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	nodePtr checkPtr = *head;
	nodePtr currentPtr = *head;
	nodePtr reverse_list = NULL;

	if (!head || !currentPtr)
	{
		return (1);
	}
	while (currentPtr)
	{
		add_node(&reverse_list, currentPtr->n);
		currentPtr = currentPtr->next;
	}
	currentPtr = *head;
	checkPtr = reverse_list;

	while (currentPtr)
	{
		if (currentPtr->n != checkPtr->n)
		{
			return (0);
		}
		currentPtr = currentPtr->next;
		checkPtr = checkPtr->next;
	}
	return (1);
}

