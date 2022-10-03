/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        
        struct ListNode *i =head;
        struct ListNode *j =head;
        while (j!=NULL && j->next !=NULL){
            i=i->next;
            j=j->next->next;
            
        }
        return i;
    }
};