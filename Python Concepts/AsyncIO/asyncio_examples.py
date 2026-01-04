"""
AsyncIO Practical Examples
==========================

This file contains working examples of AsyncIO concepts covered in the tutorial.
Run different functions to see AsyncIO in action.

Requirements:
    pip install aiohttp aiofiles

Usage:
    python asyncio_examples.py
"""

import asyncio
import aiohttp
import aiofiles
import time
import random
from typing import List


# Basic AsyncIO Examples
async def basic_hello():
    """Basic async function example"""
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def fetch_data(url: str, delay: float = 1.0) -> str:
    """Simulate fetching data from an API"""
    print(f"Fetching data from {url}...")
    await asyncio.sleep(delay)
    return f"Data from {url}"


# Concurrent Execution Examples
async def sequential_vs_concurrent():
    """Compare sequential vs concurrent execution"""
    urls = ["api1", "api2", "api3"]
    
    # Sequential execution
    print("=== Sequential Execution ===")
    start_time = time.time()
    results_sequential = []
    for url in urls:
        result = await fetch_data(url)
        results_sequential.append(result)
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f} seconds")
    
    # Concurrent execution
    print("\n=== Concurrent Execution ===")
    start_time = time.time()
    results_concurrent = await asyncio.gather(*[fetch_data(url) for url in urls])
    concurrent_time = time.time() - start_time
    print(f"Concurrent time: {concurrent_time:.2f} seconds")
    
    print(f"\nSpeedup: {sequential_time/concurrent_time:.2f}x")


# Real HTTP Requests Example
async def fetch_real_url(session: aiohttp.ClientSession, url: str) -> dict:
    """Fetch real URL using aiohttp"""
    try:
        async with session.get(url) as response:
            return {
                'url': url,
                'status': response.status,
                'content_length': len(await response.text())
            }
    except Exception as e:
        return {'url': url, 'error': str(e)}


async def web_scraping_example():
    """Example of concurrent web scraping"""
    urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2'
    ]
    
    print("=== Web Scraping Example ===")
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch_real_url(session, url) for url in urls])
    
    end_time = time.time()
    
    for result in results:
        print(f"URL: {result['url']}")
        if 'error' in result:
            print(f"  Error: {result['error']}")
        else:
            print(f"  Status: {result['status']}, Length: {result['content_length']}")
    
    print(f"\nTotal time: {end_time - start_time:.2f} seconds")


# Task Management Examples
async def task_management_example():
    """Example of creating and managing tasks"""
    print("=== Task Management Example ===")
    
    # Create tasks
    task1 = asyncio.create_task(fetch_data("task1", 2))
    task2 = asyncio.create_task(fetch_data("task2", 1))
    task3 = asyncio.create_task(fetch_data("task3", 1.5))
    
    # Wait for all tasks
    results = await asyncio.gather(task1, task2, task3)
    
    for result in results:
        print(result)


# Error Handling Example
async def risky_operation(success_rate: float = 0.7) -> str:
    """Operation that might fail"""
    await asyncio.sleep(random.uniform(0.5, 1.5))
    if random.random() < success_rate:
        return "Success!"
    else:
        raise Exception("Operation failed!")


async def error_handling_example():
    """Example of handling errors in async operations"""
    print("=== Error Handling Example ===")
    
    tasks = [risky_operation() for _ in range(5)]
    
    for i, task in enumerate(asyncio.as_completed(tasks)):
        try:
            result = await task
            print(f"Task {i+1}: {result}")
        except Exception as e:
            print(f"Task {i+1}: Error - {e}")


# Timeout Example
async def slow_operation(delay: float) -> str:
    """Simulate a slow operation"""
    await asyncio.sleep(delay)
    return f"Completed after {delay} seconds"


async def timeout_example():
    """Example of using timeouts"""
    print("=== Timeout Example ===")
    
    operations = [
        slow_operation(1),
        slow_operation(3),
        slow_operation(5)
    ]
    
    for i, operation in enumerate(operations):
        try:
            result = await asyncio.wait_for(operation, timeout=2.0)
            print(f"Operation {i+1}: {result}")
        except asyncio.TimeoutError:
            print(f"Operation {i+1}: Timed out!")


# Rate Limiting Example
async def rate_limited_fetch(semaphore: asyncio.Semaphore, url: str) -> str:
    """Fetch with rate limiting using semaphore"""
    async with semaphore:
        return await fetch_data(url, 0.5)


async def rate_limiting_example():
    """Example of rate limiting with semaphores"""
    print("=== Rate Limiting Example ===")
    
    # Allow only 2 concurrent operations
    semaphore = asyncio.Semaphore(2)
    urls = [f"api{i}" for i in range(6)]
    
    start_time = time.time()
    results = await asyncio.gather(*[rate_limited_fetch(semaphore, url) for url in urls])
    end_time = time.time()
    
    for result in results:
        print(result)
    
    print(f"Total time with rate limiting: {end_time - start_time:.2f} seconds")


# File I/O Example
async def file_io_example():
    """Example of async file operations"""
    print("=== File I/O Example ===")
    
    # Create test files
    filenames = ['test1.txt', 'test2.txt', 'test3.txt']
    
    # Write files concurrently
    write_tasks = []
    for i, filename in enumerate(filenames):
        content = f"This is content for file {i+1}\nLine 2 of file {i+1}"
        write_tasks.append(write_file_async(filename, content))
    
    await asyncio.gather(*write_tasks)
    print("Files written concurrently")
    
    # Read files concurrently
    read_tasks = [read_file_async(filename) for filename in filenames]
    contents = await asyncio.gather(*read_tasks)
    
    for filename, content in zip(filenames, contents):
        print(f"\n{filename}:")
        print(content)


async def write_file_async(filename: str, content: str):
    """Write file asynchronously"""
    async with aiofiles.open(filename, 'w') as file:
        await file.write(content)


async def read_file_async(filename: str) -> str:
    """Read file asynchronously"""
    try:
        async with aiofiles.open(filename, 'r') as file:
            return await file.read()
    except FileNotFoundError:
        return f"File {filename} not found"


# Producer-Consumer Example
async def producer(queue: asyncio.Queue, name: str):
    """Producer that adds items to queue"""
    for i in range(5):
        item = f"{name}-item-{i}"
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.5)
    
    # Signal completion
    await queue.put(None)


async def consumer(queue: asyncio.Queue, name: str):
    """Consumer that processes items from queue"""
    while True:
        item = await queue.get()
        if item is None:
            # Signal to stop
            await queue.put(None)
            break
        
        print(f"Consumer {name} processing: {item}")
        await asyncio.sleep(1)  # Simulate processing time
        queue.task_done()


async def producer_consumer_example():
    """Example of producer-consumer pattern"""
    print("=== Producer-Consumer Example ===")
    
    queue = asyncio.Queue(maxsize=3)
    
    # Create producer and consumers
    producer_task = asyncio.create_task(producer(queue, "Producer1"))
    consumer1_task = asyncio.create_task(consumer(queue, "Consumer1"))
    consumer2_task = asyncio.create_task(consumer(queue, "Consumer2"))
    
    # Wait for producer to finish
    await producer_task
    
    # Wait for consumers to finish processing
    await queue.join()
    
    # Cancel consumers
    consumer1_task.cancel()
    consumer2_task.cancel()


# Main function to run examples
async def main():
    """Run all examples"""
    examples = [
        ("Basic Hello", basic_hello),
        ("Sequential vs Concurrent", sequential_vs_concurrent),
        ("Task Management", task_management_example),
        ("Error Handling", error_handling_example),
        ("Timeout Example", timeout_example),
        ("Rate Limiting", rate_limiting_example),
        ("File I/O", file_io_example),
        ("Producer-Consumer", producer_consumer_example),
    ]
    
    print("AsyncIO Examples Demo")
    print("=" * 50)
    
    for name, example_func in examples:
        print(f"\n{'='*20} {name} {'='*20}")
        try:
            await example_func()
        except Exception as e:
            print(f"Error in {name}: {e}")
        
        print("\n" + "."*50)
        await asyncio.sleep(1)  # Pause between examples
    
    # Run web scraping example separately (requires internet)
    print(f"\n{'='*20} Web Scraping Example {'='*20}")
    try:
        await web_scraping_example()
    except Exception as e:
        print(f"Web scraping example failed (might need internet): {e}")


if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())