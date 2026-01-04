# AsyncIO in Python - Complete Guide

## Table of Contents
1. [What is AsyncIO?](#what-is-asyncio)
2. [Key Concepts](#key-concepts)
3. [Basic Syntax](#basic-syntax)
4. [Common Patterns](#common-patterns)
5. [Real-World Examples](#real-world-examples)
6. [Best Practices](#best-practices)
7. [Common Pitfalls](#common-pitfalls)

## What is AsyncIO?

AsyncIO is Python's built-in library for writing concurrent code using the async/await syntax. It's particularly useful for I/O-bound operations like:
- Network requests
- File operations
- Database queries
- Web scraping

### Why Use AsyncIO?
- **Performance**: Handle thousands of concurrent operations
- **Efficiency**: Single-threaded but non-blocking
- **Scalability**: Better resource utilization than threading for I/O-bound tasks

## Key Concepts

### 1. Coroutines
Functions defined with `async def` that can be paused and resumed.

```python
async def my_coroutine():
    return "Hello AsyncIO"
```

### 2. Event Loop
The heart of AsyncIO that manages and executes coroutines.

### 3. Awaitable Objects
Objects that can be used with the `await` keyword:
- Coroutines
- Tasks
- Futures

### 4. Tasks
Wrapped coroutines that can run concurrently.

## Basic Syntax

### Creating and Running Coroutines

```python
import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Python 3.7+
asyncio.run(hello())

# Older versions
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
```

### Awaiting Multiple Coroutines

```python
async def fetch_data(url):
    await asyncio.sleep(1)  # Simulate network request
    return f"Data from {url}"

async def main():
    # Sequential execution
    result1 = await fetch_data("url1")
    result2 = await fetch_data("url2")
    
    # Concurrent execution
    results = await asyncio.gather(
        fetch_data("url1"),
        fetch_data("url2"),
        fetch_data("url3")
    )
    print(results)

asyncio.run(main())
```

## Common Patterns

### 1. asyncio.gather()
Run multiple coroutines concurrently and collect results.

```python
async def main():
    results = await asyncio.gather(
        fetch_data("api1"),
        fetch_data("api2"),
        fetch_data("api3")
    )
    return results
```

### 2. asyncio.create_task()
Create tasks for concurrent execution.

```python
async def main():
    task1 = asyncio.create_task(fetch_data("api1"))
    task2 = asyncio.create_task(fetch_data("api2"))
    
    result1 = await task1
    result2 = await task2
```

### 3. asyncio.wait_for()
Add timeout to operations.

```python
async def main():
    try:
        result = await asyncio.wait_for(fetch_data("slow_api"), timeout=5.0)
    except asyncio.TimeoutError:
        print("Operation timed out")
```

### 4. asyncio.as_completed()
Process results as they complete.

```python
async def main():
    tasks = [fetch_data(f"api{i}") for i in range(5)]
    
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"Completed: {result}")
```

## Real-World Examples

### Web Scraping with aiohttp

```python
import aiohttp
import asyncio

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Usage
urls = ["http://example.com", "http://google.com"]
results = asyncio.run(scrape_multiple_urls(urls))
```

### Database Operations

```python
import asyncpg
import asyncio

async def fetch_users(pool):
    async with pool.acquire() as connection:
        return await connection.fetch("SELECT * FROM users")

async def main():
    pool = await asyncpg.create_pool("postgresql://user:pass@localhost/db")
    users = await fetch_users(pool)
    await pool.close()
```

### File I/O with aiofiles

```python
import aiofiles
import asyncio

async def read_file(filename):
    async with aiofiles.open(filename, 'r') as file:
        content = await file.read()
        return content

async def write_file(filename, content):
    async with aiofiles.open(filename, 'w') as file:
        await file.write(content)

async def process_files():
    # Read multiple files concurrently
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    contents = await asyncio.gather(*[read_file(f) for f in files])
    return contents
```

## Best Practices

### 1. Use asyncio.run() for Entry Point
```python
# Good
async def main():
    # Your async code here
    pass

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. Don't Mix Blocking and Non-blocking Code
```python
# Bad
async def bad_example():
    time.sleep(1)  # Blocks the entire event loop
    
# Good
async def good_example():
    await asyncio.sleep(1)  # Non-blocking
```

### 3. Use Context Managers for Resources
```python
async def good_resource_management():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://example.com') as response:
            return await response.text()
```

### 4. Handle Exceptions Properly
```python
async def safe_operation():
    try:
        result = await risky_operation()
        return result
    except Exception as e:
        logger.error(f"Operation failed: {e}")
        return None
```

### 5. Use Semaphores for Rate Limiting
```python
async def rate_limited_requests(urls, max_concurrent=5):
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def fetch_with_limit(url):
        async with semaphore:
            return await fetch_url(url)
    
    tasks = [fetch_with_limit(url) for url in urls]
    return await asyncio.gather(*tasks)
```

## Common Pitfalls

### 1. Forgetting await
```python
# Wrong - returns coroutine object
result = fetch_data()

# Correct
result = await fetch_data()
```

### 2. Using Blocking Operations
```python
# Wrong - blocks event loop
requests.get('http://example.com')

# Correct - use async library
async with aiohttp.ClientSession() as session:
    async with session.get('http://example.com') as response:
        data = await response.text()
```

### 3. Not Handling Task Cancellation
```python
async def cancellable_task():
    try:
        while True:
            await asyncio.sleep(1)
            # Do work
    except asyncio.CancelledError:
        # Cleanup code
        raise
```

### 4. Creating Too Many Tasks
```python
# Bad - creates thousands of tasks at once
tasks = [asyncio.create_task(fetch_url(url)) for url in huge_url_list]

# Good - use semaphore or process in batches
semaphore = asyncio.Semaphore(10)
async def limited_fetch(url):
    async with semaphore:
        return await fetch_url(url)
```

## Performance Tips

1. **Use asyncio.gather()** for concurrent execution
2. **Implement connection pooling** for database/HTTP operations
3. **Use semaphores** to limit concurrent operations
4. **Profile your code** to identify bottlenecks
5. **Consider using asyncio.Queue** for producer-consumer patterns

## Debugging AsyncIO

### Enable Debug Mode
```python
import asyncio
import logging

# Enable debug mode
asyncio.run(main(), debug=True)

# Or set event loop debug
loop = asyncio.get_event_loop()
loop.set_debug(True)
```

### Common Debug Techniques
- Use `asyncio.current_task()` to inspect running tasks
- Check for unawaited coroutines
- Monitor event loop with `loop.slow_callback_duration`

## Conclusion

AsyncIO is powerful for I/O-bound concurrent programming in Python. Key takeaways:

- Use `async def` and `await` for asynchronous operations
- Leverage `asyncio.gather()` and `asyncio.create_task()` for concurrency
- Always use async libraries (aiohttp, asyncpg, aiofiles)
- Handle exceptions and cancellation properly
- Use semaphores for rate limiting

Start with simple examples and gradually build complexity. AsyncIO shines in scenarios with many I/O operations that can be parallelized.

## Further Reading

- [Official AsyncIO Documentation](https://docs.python.org/3/library/asyncio.html)
- [Real Python AsyncIO Tutorial](https://realpython.com/async-io-python/)
- [AsyncIO Best Practices](https://docs.python.org/3/library/asyncio-dev.html)

---

*Happy Async Programming! 🚀*