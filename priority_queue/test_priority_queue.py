import heapq


def main():
    print("--- Test built in Priority Queue ---\n")

    pq = []

    heapq.heappush(pq, (3, "Task 3"))
    heapq.heappush(pq, (1, "Task 1"))
    heapq.heappush(pq, (2, "Task 2"))

    while pq:
        priority, task = heapq.heappop(pq)
        print(f'Priority: {priority}, task: {task}')



if __name__ == "__main__":
    main()


