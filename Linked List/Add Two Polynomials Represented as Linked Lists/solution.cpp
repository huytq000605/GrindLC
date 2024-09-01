/**
 * Definition for polynomial singly-linked list.
 * struct PolyNode {
 *     int coefficient, power;
 *     PolyNode *next;
 *     PolyNode(): coefficient(0), power(0), next(nullptr) {};
 *     PolyNode(int x, int y): coefficient(x), power(y), next(nullptr) {};
 *     PolyNode(int x, int y, PolyNode* next): coefficient(x), power(y), next(next) {};
 * };
 */

class Solution {
public:
    PolyNode* addPoly(PolyNode* poly1, PolyNode* poly2) {
        PolyNode* head;
        PolyNode** cur = &head;
        auto add = [&](int power, int coeff) {
            if(!coeff) return;
            *cur = new PolyNode(coeff, power);
            cur = &(*cur)->next;
        };
        while(poly1 || poly2) {
            if(!poly1 || (poly2 && poly2->power > poly1->power)) {
                add(poly2->power, poly2->coefficient);
                poly2 = poly2->next;
            } else if(!poly2 || poly1->power > poly2->power) {
                add(poly1->power, poly1->coefficient);
                poly1 = poly1->next;
            } else {
                add(poly2->power, poly2->coefficient + poly1->coefficient);
                poly2 = poly2->next;
                poly1 = poly1->next;
            }
        }
        return head;
    }
};
