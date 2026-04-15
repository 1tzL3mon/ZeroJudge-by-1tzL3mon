#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Node {
    Node *prev, *next;
    string name;

    Node(string name_ = "") :
    prev(NULL), next(NULL), name(name_) { } //建構子，初始化指標為 NULL 並設定名字。
};

Node* nil; //宣告一個全域的哨兵節點指標

void init() {
    nil = new Node(); //建立哨兵
    nil->prev = nil; //讓哨兵的的前後都指向自己，形成一個空的循環
    nil->next = nil;
}

void printList() {
    Node* cur = nil->next; //（第一個真正存資料的節點）開始，直到回到 nil 為止
    for (; cur != nil; cur = cur->next) {
        cout << cur->name << " -> ";
    }
    cout << endl;
}

void insert(Node* v, Node* p = nil) { //將節點 v 插入到節點 p 之後。
                                        //預設 p = nil 表示插入到串列的最前面。
    v->next = p->next;
    p->next->prev = v;
    p->next = v;
    v->prev = p;
}

void erase(Node *v) { //刪除節點 v。
                        //調整 v 前後節點的指向，使其跳過 v，最後 delete v
    if (v == nil) return;
    v->prev->next = v->next;
    v->next->prev = v->prev;
    delete v;
}

int main() {
    init();

    vector<string> names = {"yamamoto",
                            "watanabe",
                            "ito",
                            "takahashi",
                            "suzuki",
                            "sato"};

    Node *watanabe;
    for (int i = 0; i < (int)names.size(); ++i) { //遍歷名字，為每個名字建立 new Node，並呼叫 insert 放入串列
        Node* node = new Node(names[i]);

        insert(node);

        if (names[i] == "watanabe") watanabe = node; //當名字是 "watanabe" 時，用指針記錄該節點位置
    }

    cout << "before: "; //執行結果： 印出刪除 "watanabe" 前後的串列狀態
    printList();
    erase(watanabe);
    cout << "after: ";
    printList();
}
