/* 
Descrption:
问题描述:
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
*/



//Solution One 自己写的垃圾程序
#include <iostream>
using namespace std;
struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL) {}
};
//自己的方法
class Solution {
public:
	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
		bool step_flag = 0;
		ListNode* head = new ListNode(0);
		ListNode* current_node = new ListNode(0);
		ListNode* next_node = new ListNode(0);
		head = current_node;

		while (l1 != NULL || l2 != NULL) 
		{ //只要有一个不空
			//1.两个指针当前都不空
			ListNode* new_node = new ListNode(0);
			if (l1 != NULL && l2 != NULL) 
			{
				/*Current Node Caculate*/
				new_node->val = (l1->val + l2->val + step_flag) % 10;
				if ((l1->val + l2->val >= 10 && step_flag == 0) ||
					(l1->val + l2->val >= 9 && step_flag == 1)) {
					step_flag = 1;
				}
				else {
					step_flag = 0;
				}
				l1 = l1->next;
				l2 = l2->next;
			}
			else if (l1 == NULL) 
			{  //l1 is null
				new_node->val = (l1->val + step_flag) % 10;
				if (l1->val >= 9 && step_flag == 1) {
					step_flag = 1;
				}
				else {
					step_flag = 0;
				}
				l1 = l1->next;
			}
			else 
			{
				new_node->val = (l2->val + step_flag) % 10;
				if (l2->val >= 9 && step_flag == 1) {
					step_flag = 1;
				}
				else {
					step_flag = 0;
				}
				l2 = l2->next;
			}

			/*Next Node Generated*/
			current_node->val = new_node->val;
			current_node->next = next_node;
			next_node->next = NULL;
			current_node = next_node;
		}
		return head;
	}

	void insert_node(int val, ListNode* _head) 
	{ 
		ListNode* _next_node = new ListNode(0);
		ListNode* new_node = new ListNode(0);
		_next_node = _head;
		while (_next_node->next != NULL) {
			_next_node = _next_node->next;
		}
		new_node->val = val;
		new_node->next = NULL;
		_next_node->next = new_node;	
	}

	void print_node(ListNode* _head) 
	{
		ListNode* _current_node = new ListNode(0);
		_current_node = _head;
		while (_current_node != NULL) {
			cout << _current_node->val << " ";
			_current_node = _current_node->next;
		}
	}
};

int main() 
{
	Solution test_s;
	ListNode* head1 = new ListNode(2);
	ListNode* head2 = new ListNode(5);
	cout << "running " << endl;

	test_s.insert_node(4, head1);
	test_s.insert_node(3, head1);
	test_s.insert_node(6, head2);
	test_s.insert_node(4, head2);
	test_s.print_node(head1);
	test_s.print_node(head2);

	ListNode* res_node = new ListNode(0);
	res_node = test_s.addTwoNumbers(head1,head2);
	cout <<endl <<  "两数之和" << endl;
	test_s.print_node(res_node);
	return 0;
}
//Solution Two 递归方法  需要新链表
/* #include <iostream>
using namespace std;
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};
int c = 0;
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if(l1==NULL&&l2==NULL&&c==0)return NULL;
        if ( l1 ){
            c += l1->val,l1=l1->next;
        }
        else{
            c += 0;
        }
        if ( l2 ){
            c += l2->val,l2=l2->next;
        }
        else{
            c += 0;
        }
        ListNode *cur = new ListNode(0);
        cur->val=c%10;
        c=c/10;
        cur->next=addTwoNumbers(l1,l2);
        return cur;
    }
}; */