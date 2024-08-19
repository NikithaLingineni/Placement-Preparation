void deletenode(struct node* node)
{
    node->val=node->next->val;
    node->next=node->next->next;
}
