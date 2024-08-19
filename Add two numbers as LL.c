struct node* create(int val)
{
    struct node* newnode=(struct node*)malloc(sizeof(struct node))
    newnode->val=val;
    newnode->next=NULL;
    return newnode;
}

struct listnode* addtwo(struct node* l1,struct node* l1)
{
    struct listnode dummy;
    struct listnode* temp=&dummy;
    dummy.next=NULL;
    while(l1!=NULL || l2!=NULL || carry!=0)
    {
        int sum=0;
        if(l1!=NULL)
        {
            sum+=l1->val;
            l1=l1->next;
        }
        if(l2!=NULL)
        {
            sum+=l2->val;
            l2=l2->next;
        }
        sum+=carry;
        carry=sum/10;
        sum=sum%10;
        struct node* newnode=create(sum);
        temp->next=newnode;
        temp=temp->next;
    }
    return dummy.next;
}
