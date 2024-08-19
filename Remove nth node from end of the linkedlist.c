struct listnode* removenthode(struct node* head, int n)
{
    struct listnode* temp,*slow=head,*fast=head;
    if(head==NULL) return NULL;
    else
    {
        int c=0;
        while(fast)
        {
            while(c<n)
            {
                fast=fast->next;
                c++;
            }
            temp=slow;
            fast=fast->next;
            slow=slow->next;
        }
    }
    temp->next=slow->next;
    free(slow);
    return head;
}
