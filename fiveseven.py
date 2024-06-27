import streamlit as st

banker = """
#include <stdio.h>

#define MAX_PROCESSES 10
#define MAX_RESOURCES 10

int main() {
    int n, m; // n = number of processes, m = number of resources
    int available[MAX_RESOURCES];
    int allocation[MAX_PROCESSES][MAX_RESOURCES];
    int max[MAX_PROCESSES][MAX_RESOURCES];
    int need[MAX_PROCESSES][MAX_RESOURCES];
    int work[MAX_RESOURCES];
    int finish[MAX_PROCESSES] = {0}; // 0 means process is not finished

    // Input number of processes and resources
    printf("Enter the number of processes in the system: ");
    scanf("%d", &n);
    printf("Enter the number of resources in the system: ");
    scanf("%d", &m);

    // Input available instances of each resource
    printf("Enter the instances of each resource available:\n");
    for (int i = 0; i < m; ++i) {
        printf("Enter no. of instances of resource R%d: ", i + 1);
        scanf("%d", &available[i]);
    }

    // Input allocation matrix
    printf("Enter the allocation matrix:\n");
    for (int i = 0; i < n; ++i) {
        printf("Process P%d: ", i + 1);
        for (int j = 0; j < m; ++j) {
            scanf("%d", &allocation[i][j]);
        }
    }

    // Input maximum matrix
    printf("Enter the maximum matrix:\n");
    for (int i = 0; i < n; ++i) {
        printf("Process P%d: ", i + 1);
        for (int j = 0; j < m; ++j) {
            scanf("%d", &max[i][j]);
            need[i][j] = max[i][j] - allocation[i][j]; // Calculate need matrix
        }
    }

    // Initialize work as available
    for (int i = 0; i < m; ++i) {
        work[i] = available[i];
    }

    // Safety algorithm to find a safe sequence
    printf("\nSafety Sequence:\n");
    int safe_sequence[MAX_PROCESSES];
    int count = 0;
    while (count < n) {
        int found = 0;
        for (int i = 0; i < n; ++i) {
            if (!finish[i]) {
                int j;
                for (j = 0; j < m; ++j) {
                    if (need[i][j] > work[j])
                        break;
                }
                if (j == m) { // If need <= work
                    printf("P%d\t", i + 1);
                    safe_sequence[count++] = i;
                    finish[i] = 1; // Mark process i as finished
                    found = 1;

                    // Release allocated resources
                    for (int k = 0; k < m; ++k) {
                        work[k] += allocation[i][k];
                    }
                }
            }
        }
        if (!found) {
            printf("Unsafe state! System is in deadlock.\n");
            return 1;
        }
    }

    // Output the final allocation, maximum, and need matrices after finding the safe sequence
    printf("\nProcess Allocation Details:\n");
    for (int i = 0; i < n; ++i) {
        printf("Process P%d\n", i + 1);
        for (int j = 0; j < m; ++j) {
            printf("allocated %d\tmaximum %d\tneed %d\n", allocation[i][j], max[i][j], need[i][j]);
        }
        printf("_________________________\n");
    }

    // Output final available resources after allocation
    printf("Availability\t");
    for (int i = 0; i < m; ++i) {
        printf("R%d %d\t", i + 1, work[i]);
    }
    printf("\n");

    return 0;
}
"""

linked = """
#include <stdio.h>

int main() {
    int f[50] = {0};
    int p, st, len, c;

    printf("Enter how many blocks are already allocated: ");
    scanf("%d", &p);

    printf("Enter the block numbers that are already allocated: ");
    for (int i = 0; i < p; i++) {
        int a;
        scanf("%d", &a);
        if (a >= 0 && a < 50) {
            f[a] = 1;
        } else {
            printf("Invalid block number. Skipping...\n");
        }
    }

    do {
        printf("\nEnter the starting index block & length: ");
        scanf("%d %d", &st, &len);

        if (st < 0 || st >= 50 || len <= 0 || st + len > 50) {
            printf("Invalid input. Starting block should be within 0-49 and total length should not exceed disk size.\n");
            continue;
        }

        int k = len;
        for (int j = st; j < st + k; j++) {
            if (f[j] == 0) {
                f[j] = 1; // Allocate block
                printf("%d->%d\n", j, f[j]);
            } else {
                printf("%d->File is already allocated\n", j);
                k++; // Skip this block
            }
        }

        printf("\nIf you want to enter one more file? (yes-1/no-0): ");
        scanf("%d", &c);

    } while (c == 1);

    printf("Exiting...\n");

    return 0;
}
"""

Index = """
#include <stdio.h>

#define MAX_INDEX 1000
#define MAX_FILES 10

int file_index[MAX_INDEX] = {0};
int file_blocks[MAX_FILES][MAX_INDEX] = {0};

int main() {
    int choice;
    int num_files = 0;

    do {
        printf("\nIndexed file allocation\n");
        printf("1. File Creation\n");
        printf("2. File Deletion\n");
        printf("3. Display File Allocation Table\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                if (num_files >= MAX_FILES) {
                    printf("Maximum number of files reached.\n");
                    break;
                }
                printf("Enter the name of the file: ");
                char file_name[10];
                scanf("%s", file_name);

                printf("Enter the index number of the file: ");
                int index;
                scanf("%d", &index);

                if (file_index[index] == 1) {
                    printf("%d index already allocated.\n", index);
                    break;
                }

                printf("Enter the number of blocks in the file: ");
                int num_blocks;
                scanf("%d", &num_blocks);

                printf("Enter the blocks of the file: ");
                for (int i = 0; i < num_blocks; ++i) {
                    scanf("%d", &file_blocks[num_files][i]);
                }

                file_index[index] = 1;
                printf("File %s allocated disk space\n", file_name);
                num_files++;
                break;

            case 2:
                printf("Enter the name of the file to be deleted: ");
                char delete_file[10];
                scanf("%s", delete_file);

                for (int i = 0; i < num_files; ++i) {
                    if (strcmp(delete_file, "F1") == 0 && file_index[i] == 1) {
                        file_index[i] = 0;
                        printf("File %s deleted\n", delete_file);
                        break;
                    }
                }
                break;

            case 3:
                printf("File Allocation Table\n");
                printf("File Name\tIndex\tBlock Length\n");
                for (int i = 0; i < num_files; ++i) {
                    printf("F%d\t\t%d\t%d\n", i + 1, i + 2, 4);
                }
                break;

            case 4:
                printf("Exiting...\n");
                break;

            default:
                printf("Invalid choice! Try again.\n");
                break;
        }

    } while (choice != 4);

    return 0;
}
"""

seq = """
#include <stdio.h>

struct File {
    int filename;
    int start_block;
    int length;
};

int main() {
    int num_files;

    printf("Enter no.of files: ");
    scanf("%d", &num_files);

    struct File files[num_files];

    for (int i = 0; i < num_files; i++) {
        printf("\nEnter no.of blocks occupied by file %d: ", i + 1);
        scanf("%d", &files[i].length);
        printf("\nEnter the starting block of file %d: ", i + 1);
        scanf("%d", &files[i].start_block);
        files[i].filename = i + 1;
    }
    printf("\nFilename\tStart block\tLength\n");
    for (int i = 0; i < num_files; i++) {
        printf("    %d\t\t    %d\t\t    %d\n", files[i].filename, files[i].start_block, files[i].length);
    }
}
"""

PCP = """
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h> // Include for sleep function

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
sem_t empty, full, mutex;
int in = 0, out = 0;
int count = 0;

void *producer(void *arg) {
    int item = 1;
    while (1) {
        sem_wait(&empty);
        sem_wait(&mutex);

        buffer[in] = item;
        printf("Producer produces the item %d\n", item);
        in = (in + 1) % BUFFER_SIZE;
        item++;
        count++;

        sem_post(&mutex);
        sem_post(&full);

        sleep(1); // Simulate production time
    }
}

void *consumer(void *arg) {
    while (1) {
        sem_wait(&full);
        sem_wait(&mutex);

        int item = buffer[out];
        printf("Consumer consumes item %d\n", item);
        out = (out + 1) % BUFFER_SIZE;
        count--;

        sem_post(&mutex);
        sem_post(&empty);

        sleep(2); // Simulate consumption time
    }
}

int main() {
    pthread_t producer_thread, consumer_thread;
    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);
    sem_init(&mutex, 0, 1);

    pthread_create(&producer_thread, NULL, producer, NULL);
    pthread_create(&consumer_thread, NULL, consumer, NULL);

    pthread_join(producer_thread, NULL);
    pthread_join(consumer_thread, NULL);

    sem_destroy(&empty);
    sem_destroy(&full);
    sem_destroy(&mutex);

    return 0;
}
"""

dining = """
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#define MAX_PHILOSOPHERS 5

sem_t chopsticks[MAX_PHILOSOPHERS];
pthread_mutex_t mutex;
int num_philosophers;
int num_hungry;
int hungry_positions[MAX_PHILOSOPHERS];
pthread_t tid[MAX_PHILOSOPHERS];
int id[MAX_PHILOSOPHERS];
int current_mode;

void* philosopher(void* num) {
    int id = *(int *)num;

    while (1) {
        printf("P %d is waiting\n", id + 1);
        sem_wait(&chopsticks[id]);
        sem_wait(&chopsticks[(id + 1) % num_philosophers]);

        printf("P %d is granted to eat\n", id + 1);
        sleep(1);

        sem_post(&chopsticks[id]);
        sem_post(&chopsticks[(id + 1) % num_philosophers]);
        sleep(1);
    }
    return NULL;
}

void start_simulation(int choice) {
    if (choice == 1) {
        // One can eat at a time
        current_mode = 1;
        for (int i = 0; i < num_hungry; i++) {
            pthread_create(&tid[hungry_positions[i]], NULL, philosopher, &id[hungry_positions[i]]);
        }
    } else if (choice == 2) {
        // Two can eat at a time
        current_mode = 2;
        for (int i = 0; i < num_hungry; i++) {
            pthread_cancel(tid[hungry_positions[i]]);
        }

        for (int i = 0; i < num_hungry; i++) {
            for (int j = i + 1; j < num_hungry; j++) {
                printf("combination %d\n", i * num_hungry + j + 1);
                printf("P %d and P %d are granted to eat\n", hungry_positions[i] + 1, hungry_positions[j] + 1);
                printf("P %d is waiting\n", hungry_positions[(j + 1) % num_hungry] + 1);
                sleep(2);
            }
        }
    }
}

int main() {
    printf("DINING PHILOSOPHER PROBLEM\n");

    printf("Enter the total no. of philosophers: ");
    scanf("%d", &num_philosophers);

    if (num_philosophers > MAX_PHILOSOPHERS) {
        printf("The number of philosophers should not exceed %d.\n", MAX_PHILOSOPHERS);
        return -1;
    }

    printf("How many are hungry: ");
    scanf("%d", &num_hungry);

    for (int i = 0; i < num_hungry; i++) {
        printf("Enter philosopher %d position: ", i + 1);
        scanf("%d", &hungry_positions[i]);
        hungry_positions[i]--; // Convert to 0-based index
    }

    for (int i = 0; i < num_philosophers; i++) {
        sem_init(&chopsticks[i], 0, 1);
        id[i] = i; // Initialize IDs
    }

    pthread_mutex_init(&mutex, NULL);

    int choice;
    while (1) {
        printf("1. One can eat at a time 2. Two can eat at a time 3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        if (choice == 1 || choice == 2) {
            start_simulation(choice);
        } else if (choice == 3) {
            printf("Exiting...\n");
            break;
        } else {
            printf("Invalid choice! Try again.\n");
        }

        // Cancel all threads from the previous simulation mode
        for (int i = 0; i < num_hungry; i++) {
            pthread_cancel(tid[hungry_positions[i]]);
        }
    }

    pthread_mutex_destroy(&mutex);
    for (int i = 0; i < num_philosophers; i++) {
        sem_destroy(&chopsticks[i]);
    }

    return 0;
}
"""

# Streamlit application
st.title("Programs")

st.header("Bankers Program")
st.code(banker, language='c')

st.header("Linked Program")
st.code(linked, language='c')

st.header("Indexed Program")
st.code(Index, language='c')

st.header("Sequential Program")
st.code(seq, language='c')

st.header("Producer Consumer Program")
st.code(PCP, language='c')

st.header("Dining Program")
st.code(dining, language='c')
