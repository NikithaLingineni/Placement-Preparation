struct listnode* intersection(struct node* headA,struct node* headB)
{
    struct listnode* temp1=headA,*temp2=headB;
    if(temp1==NULL || temp2==NULL) return NULL;
    while(temp1!=temp2)
    {
        temp1=temp1->next;
        temp2=temp2->next;
        if(temp1==temp2) return temp1;
        if(temp1==NULL) temp1=headB;
        if(temp2==NULL) temp2=headA;
    }
    return temp1;
}
