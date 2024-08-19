struct node
{
	int val;
	struct node*next;
};
struct node*head,*temp,*prevnode=NULL,*nextnode,*res;
struct node* mergetwosorted(struct node *list1,struct node *list2) 
{
    struct node dummy;
    dummy.next=NULL;
    struct node* next=dummy;
    while(list1!=NULL && list2!=NULL)
    {
        if(list1->val < list2->val)
        {
            temp->next=list1;
            list1=list1->next;
        }
        else
        {
            temp->next=list2;
            list2=list2->next;
        }
        temp=temp->next;
    }
    if(list1!=NULL)
    {
        temp->next=list1;
    }
    if(list2!=NULL)
    {
        temp->next=list2;
    }
    return dummy.next;
}

struct node* mergeksorted(struct node* lists,int listssize)
{
    if(listssize==0) return NULL;
    if(listssize==1) return lists[0];
    struct node* merge=lists[0];
    for(int i=0;i<listssize;i++)
    {
        merge=mergetwosorted(merge,lists[i])
    }
    return merge;
}
