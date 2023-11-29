#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted linked list
 * @head: "listint_t **" A pointer to the head pointer of the list
 * @number: "int" The number to be inserted as a new node
 *
 * Return: "listint_t *" A pointer to the list
*/
listint_t *insert_node(listint_t **head, int number)
{
	nodePtr currentPtr = *head;
	nodePtr newPtr = malloc(sizeof(listint_t));

	newPtr->n = number;
	newPtr->next = NULL;

	if (!head || !currentPtr)
	{
		*head = newPtr;
		return (*head);
	}

	while (currentPtr)
	{
		if (currentPtr->next && (currentPtr->next->n < number))
		{
			currentPtr = currentPtr->next;
			continue;
		}
		newPtr->next = currentPtr->next;
		currentPtr->next = newPtr;
		break;
	}

	return (*head);
}

