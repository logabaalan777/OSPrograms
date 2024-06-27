import streamlit as st

calculator = """
#include <stdio.h>

int main() {
    int a, b;
    char op;

    // Read inputs
    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter operator: ");
    scanf(" %c", &op);
    printf("Enter second number: ");
    scanf("%d", &b);

    switch (op) {
        case '+':
            printf("The sum is %d\n", a + b);
            break;
        case '-':
            printf("The difference is %d\n", a - b);
            break;
        case '*':
            printf("The product is %d\n", a * b);
            break;
        case '/':
            if (b != 0)
                printf("The quotient is %d\n", a / b);
            else
                printf("Error: Division by zero\n");
            break;
        case '%':
            if (b != 0)
                printf("The remainder is %d\n", a % b);
            else
                printf("Error: Division by zero\n");
            break;
        default:
            printf("Invalid Input\n");
            break;
    }

    return 0;
}
"""

prime = """
#include <stdio.h>
#include <stdbool.h>

// Function to check if a number is prime
bool isPrime(int num) {
    if (num <= 1) return false;
    if (num == 2) return true;
    if (num % 2 == 0) return false;
    for (int i = 3; i * i <= num; i += 2) {
        if (num % i == 0) return false;
    }
    return true;
}

int main() {
    int n;
    printf("Enter the number of terms: ");
    scanf("%d", &n);

    int count = 0;
    int number = 2;

    while (count < n) {
        if (isPrime(number)) {
            printf("%d ", number);
            count++;
        }
        number++;
    }

    return 0;
}
"""

childparent = """
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
void main()
{
    int i, status;
    pid_t pid;
    pid = fork();
    if (pid < 0)
    {
        printf("\nProcess creation failure\n");
    }
    else if(pid > 0)
    {
        wait(NULL);
        printf ("\nParent starts\nEven Nos: ");
        for (i=2;i<=10;i+=2)
            printf ("%3d",i);
        printf ("\nParent ends\n");
    }
    else if (pid == 0)
    {
        printf ("Child starts\nOdd Nos: ");
        for (i=1;i<10;i+=2)
            printf ("%3d",i);
        printf ("\nChild ends\n");
    }
}
"""

FCFS = """
#include <stdio.h>

struct Process {
    char name;
    int burst_time;
    int arrival_order;
    int waiting_time;
    int turnaround_time;
};

void calculateTimes(struct Process *p1, struct Process *p2) {
    p1->waiting_time = 0;
    p1->turnaround_time = p1->burst_time;
    // Waiting time for process 2 based on the completion time of process 1
    p2->waiting_time = p1->burst_time;
    p2->turnaround_time = p2->waiting_time + p2->burst_time;
}

int main() {
    struct Process p1, p2, temp;
    printf("Enter the name of process 1: ");
    scanf(" %c", &p1.name);
    printf("Enter the burst time of process 1: ");
    scanf("%d", &p1.burst_time);
    printf("Enter the arrival order of process 1: ");
    scanf("%d", &p1.arrival_order);
    printf("Enter the name of process 2: ");
    scanf(" %c", &p2.name);
    printf("Enter the burst time of process 2: ");
    scanf("%d", &p2.burst_time);
    printf("Enter the arrival order of process 2: ");
    scanf("%d", &p2.arrival_order);

    // Arrange processes based on arrival order
    if (p1.arrival_order > p2.arrival_order) {
        temp = p1;
        p1 = p2;
        p2 = temp;
    }

    calculateTimes(&p1, &p2);

    printf("\nProcess Details\n");
    // Printing the table header
    printf("%-12s %-15s %-15s %-15s %-15s\n", "Process Name", "CPU Burst Time", "Arrival Order", "Waiting Time", "Turnaround Time");
    // Printing process details
    printf("%-12c %-15d %-15d %-15d %-15d\n", p1.name, p1.burst_time, p1.arrival_order, p1.waiting_time, p1.turnaround_time);
    printf("%-12c %-15d %-15d %-15d %-15d\n", p2.name, p2.burst_time, p2.arrival_order, p2.waiting_time, p2.turnaround_time);

    return 0;
}
"""

SJF = """
#include <stdio.h>
#include <string.h>

struct Process {
    char name[10];
    int burst_time;
    int arrival_order;
    int waiting_time;
    int turnaround_time;
};

void sort_by_burst_time(struct Process *p, int n) {
    struct Process temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (p[j].burst_time > p[j + 1].burst_time) {
                temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }
}

void calculate_waiting_turnaround_time(struct Process *p, int n) {
    p[0].waiting_time = 0;
    p[0].turnaround_time = p[0].burst_time;
    for (int i = 1; i < n; i++) {
        p[i].waiting_time = p[i - 1].waiting_time + p[i - 1].burst_time;
        p[i].turnaround_time = p[i].waiting_time + p[i].burst_time;
    }
}

int main() {
    struct Process processes[2];
    float avg_waiting_time, avg_turnaround_time;
    for (int i = 0; i < 2; i++) {
        printf("Enter the name of process %d: ", i + 1);
        scanf("%s", processes[i].name);
        printf("Enter the burst time of process %d: ", i + 1);
        scanf("%d", &processes[i].burst_time);
        printf("Enter the arrival order of process %d: ", i + 1);
        scanf("%d", &processes[i].arrival_order);
    }

    sort_by_burst_time(processes, 2);
    calculate_waiting_turnaround_time(processes, 2);

    printf("\nProcess Details\n");
    printf("%-15s %-15s %-15s %-15s %-15s\n", "Process Name", "Burst Time", "Arrival Order", "Waiting Time", "Turnaround Time");
    for (int i = 0; i < 2; i++) {
        printf("%-15s %-15d %-15d %-15d %-15d\n", processes[i].name, processes[i].burst_time, processes[i].arrival_order, processes[i].waiting_time, processes[i].turnaround_time);
    }

    avg_waiting_time = (processes[0].waiting_time + processes[1].waiting_time) / 2.0;
    avg_turnaround_time = (processes[0].turnaround_time + processes[1].turnaround_time) / 2.0;

    printf("Average waiting time is %.2f\n", avg_waiting_time);
    printf("Average turnaround time is %.2f\n", avg_turnaround_time);

    return 0;
}
"""

priority = """
#include <stdio.h>
#include <stdlib.h>

struct Process {
    char name;
    int burst_time;
    int priority;
};

void swap(struct Process *xp, struct Process *yp) {
    struct Process temp = *xp;
    *xp = *yp;
    *yp = temp;
}

// Function to perform Selection Sort based on priority
void sortProcesses(struct Process *arr, int n) {
    int i, j;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j].priority > arr[j + 1].priority) {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

int main() {
    struct Process processes[2];
    // Input
    for (int i = 0; i < 2; i++) {
        printf("Enter the name of process %d: ", i + 1);
        scanf(" %c", &processes[i].name);
        printf("Enter the burst time of process %d: ", i + 1);
        scanf("%d", &processes[i].burst_time);
        printf("Enter the priority of process %d: ", i + 1);
        scanf("%d", &processes[i].priority);
    }

    // Sort processes based on priority
    sortProcesses(processes, 2);

    // Output
    printf("\nProcess Details\n");
    printf("%-15s %-15s %-15s\n", "Name", "Burst Time", "Priority");
    for (int i = 0; i < 2; i++) {
        printf("%-15c %-15d %-15d\n", processes[i].name, processes[i].burst_time, processes[i].priority);
    }

    return 0;
}
"""

roudrobin = """
#include <stdio.h>

#define MAX_PROCESSES 2

struct Process {
    char name;
    int burst_time;
    int remaining_time;
    int waiting_time;
    int turnaround_time;
};

void roundRobin(struct Process *processes, int n, int time_slice) {
    int total_time = 0;
    int completed = 0;

    // Initialize remaining time for all processes
    for (int i = 0; i < n; i++) {
        processes[i].remaining_time = processes[i].burst_time;
    }

    // Round Robin scheduling
    while (completed < n) {
        for (int i = 0; i < n; i++) {
            if (processes[i].remaining_time > 0) {
                if (processes[i].remaining_time > time_slice) {
                    total_time += time_slice;
                    processes[i].remaining_time -= time_slice;
                } else {
                    total_time += processes[i].remaining_time;
                    processes[i].waiting_time = total_time - processes[i].burst_time;
                    processes[i].turnaround_time = total_time;
                    processes[i].remaining_time = 0;
                    completed++;
                }
            }
        }
    }
}

int main() {
    struct Process processes[MAX_PROCESSES];
    int time_slice;

    // Input
    for (int i = 0; i < MAX_PROCESSES; i++) {
        printf("Enter the name of process %d: ", i + 1);
        scanf(" %c", &processes[i].name);
        printf("Enter the burst time of process %d: ", i + 1);
        scanf("%d", &processes[i].burst_time);
    }

    printf("Enter the time slice: ");
    scanf("%d", &time_slice);

    // Calculate waiting time and turnaround time using Round Robin algorithm
    roundRobin(processes, MAX_PROCESSES, time_slice);

    // Output
    printf("\nProcess Details\n");
    printf("%-15s %-15s %-15s %-15s\n", "Process Name", "CPU Burst Time", "Waiting Time", "Turnaround Time");
    for (int i = 0; i < MAX_PROCESSES; i++) {
        printf("%-15c %-15d %-15d %-15d\n", processes[i].name, processes[i].burst_time, processes[i].waiting_time, processes[i].turnaround_time);
    }

    return 0;
}
"""

# Streamlit application
st.title("Programs")

st.header("Calculator Program")
st.code(calculator, language='c')

st.header("Prime Program")
st.code(prime, language='c')

st.header("child parent Program")
st.code(childparent, language='c')

st.header("FCFS Program")
st.code(FCFS, language='c')

st.header("SJF Program")
st.code(SJF, language='c')

st.header("Priority Program")
st.code(priority, language='c')

st.header("Round Robin Program")
st.code(roudrobin, language='c')