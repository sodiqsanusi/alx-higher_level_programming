#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list has a cycle
 * @list: "listint_t *" The head of the list to be checked
 *
 * Return: "int" 0 if there is no cycle, 1 otherwise
*/
int check_cycle(listint_t *list)
{
	nodePtr refToHead = list;
	nodePtr currentPtr = list;

	if (!list)
	{
		return (0);
	}

	while (currentPtr)
	{
		currentPtr = currentPtr->next;
		if (currentPtr == refToHead)
		{
			return (1);
		}
	}

	return (0);
}

