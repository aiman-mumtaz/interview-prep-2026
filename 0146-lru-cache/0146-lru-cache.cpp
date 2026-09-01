class LRUCache {

public:
    class Node {
    public:
        int key;
        int value;
        Node* next;
        Node* prev;

        Node(int key, int value){
            this->key = key;
            this->value = value;
        }
    };
    Node* head = new Node(-1,-1);
    Node* tail = new Node(-1, -1);

    int capacity;
    unordered_map<int, Node*> m;

    LRUCache(int capacity) {
        this->capacity=capacity;
        this->head->next=tail;
        this->tail->prev=head;
    }
    void addNode(Node* newNode){
        Node* tmp = head->next;
        newNode->next = tmp;
        newNode->prev = head;
        head->next = newNode;
        tmp->prev=newNode;
    }
    void deleteNode(Node* delNode){
        Node* delPrev = delNode->prev;
        Node* delNext = delNode->next;
        delPrev->next = delNext;
        delNext->prev = delPrev;
    }
    int get(int key) {
        if(m.find(key) != m.end()){
            Node* resNode = m[key];
            int res = resNode->value;
            m.erase(key);
            deleteNode(resNode);
            addNode(resNode);
            m[key]=head->next;
            return res;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(m.find(key) != m.end()){
            Node* existingNode = m[key];
            m.erase(key);
            deleteNode(existingNode);
        }
        if(m.size()==capacity){
            m.erase(tail->prev->key);
            deleteNode(tail->prev);
        }
        addNode(new Node(key,value));
        m[key] = head->next;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */