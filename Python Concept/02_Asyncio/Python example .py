
import asyncio

# Define an asynchronous task
async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)  # Simulate I/O operation
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)  # Simulate I/O operation
    print("Task 2 finished")

async def task3():
    print("Task 3 started")
    await asyncio.sleep(3)  # Simulate I/O operation
    print("Task 3 finished")

# Main function to run all tasks concurrently
async def main():
    await asyncio.gather(task1(), task2(), task3())

# Running the main function with asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
