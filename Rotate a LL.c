struct listnode* rotate(struct listnode* head, int k)
{
    struct listnode* temp=head;
    if(head==NULL || head->next==NULL|| k==0) return NULL;
    int len=1;
    while(temp->next!=NULL)
    {
        len++;
        temp=temp->next;
    }
    temp->next=head;
    k=k%len;
    k=len-k;
    while(k--)
    {
        temp=temp->next;
    }
    head=temp->next;
    temp->next=NULL;
    return head;
}
