#include "lists.h"

/**
 * add_dnodeint - function that adds a new node at the beginning of a list
 * @head: current head of the list
 * @n: data of the node
 * Return: Address of the new node
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *newnode;

	newnode = malloc(sizeof(dlistint_t));

	if (newnode == NULL)
		return (NULL);

	newnode->n = n;
	newnode->next = *head;
	newnode->prev = NULL;
	*head = newnode;

	return (*head);
}
