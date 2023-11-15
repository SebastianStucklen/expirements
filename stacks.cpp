#include <iostream>
using namespace std;

string Laundry[20];
int top = -1;
int top1 = 9;
bool stop = false;

void bluepush(string clothing) {
    if (top >= 9)
        cout << "stack full" << endl;
    else
    {
        top++;
        Laundry[top] = clothing;
    }
}

void bluepop() {
    if (top <= -1)
        cout << "stack empty" << endl;
    else {
        cout << "the popped element is: " << Laundry[top] << endl;
        top--;
    }
}

void bluedisplay() {
    if (top >= 0) {
        cout << "Stack elements: ";
        for (int i = top; i >= 0; i--) {
            cout << Laundry[i] << " ";

        }
        cout << endl;
    }
    else {
        cout << "stack empty";
    }
}

void bluesize() {
    if (top >= 0 && top <= 10) {
        cout << "Stack Size: " << top + 1 << "\n";
    }
    else
        cout << "Stack empty";
}


void redpush(string clothing) {
    if (top1 >= 19)
        cout << "stack full" << endl;
    else
    {
        top1++;
        Laundry[top1] = clothing;
    }
}

void redpop() {
    if (top1 <= 10)
        cout << "stack empty" << endl;
    else {
        cout << "the popped element is " << Laundry[top1] << endl;
        top--;
    }
}

void reddisplay() {
    if (top1 >= 10) {
        cout << "Stack elements are: ";
        for (int i = top1; i >= 10; i--) {
            cout << Laundry[i] << " ";
        }
        cout << endl;
    }
    else {
        cout << "stack empty";
    }
}

void redsize() {
    if (top1 >= 10) {
        cout << "Size of the stack: " << top1 - 9 << "\n";
    }
    else
        cout << "Stack empty";
}

int main()
{

    while (stop == false)
    {
        int choice;
        string choice2;
        int choice3;
        cout << "1) push, 2) pop, 3) display, 4) size, or 5 quit" << endl;
        cin >> choice;
        switch (choice) {
            case 1:
                cout << "Type youre choice" << endl;
                cin >> choice2;
                cout << "which stack to push to? 1) blue or 2) red" << endl;
                cin >> choice3;
                if (choice3 == 1) {
                    bluepush(choice2);
                }
                else if (choice3 == 2) {
                    redpush(choice2);
                }
                break;
            case 2:
                cout << "which stack do you wish to pop? 1) blue or 2) red" << endl;
                cin >> choice3;
                if (choice3 == 1) {
                    bluepop();
                }
                else if (choice3 == 2) {
                    redpop();
                }
                break;
            case 3:
                cout << "which stack do you wish to display? 1) blue or 2) red" << endl;
                cin >> choice3;
                if (choice3 == 1) {
                    bluedisplay();
                }
                else if (choice3 == 2) {
                    reddisplay();
                }
                break;
            case 4:
                cout << "which stack do you wish to see the size of? 1) blue or 2) red" << endl;
                cin >> choice3;
                if (choice3 == 1) {
                    bluesize();
                }
                else if (choice3 == 2) {
                    redsize();
                }
                break;
            case 5:
                stop = true;
            }

    }
}