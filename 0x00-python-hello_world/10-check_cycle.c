#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: given list
 *
 * Return: 0 (False), 1 (True)
 */
int check_cycle(listint_t *list)
{
	int flag = 0;
	listint_t *refnode, *findernode;

	refnode = list;
	while (refnode != NULL)
	{
		findernode = refnode;
		while (findernode != NULL)
		{
			findernode = findernode->next;
			if (findernode == refnode)
			{
				flag = 1;
				break;
			}
		}
		if (flag)
			break;
		refnode = refnode->next;
	}
	return (flag);
}
