import time

def async_operation(name: str, duration: int) -> None:
    start_time = time.time()
    current_time = 0
    while current_time < duration:
        yield f"{name} is running"
        current_time = time.time() - start_time
        yield f"{name} is waiting"
        time.sleep(0.1)

def another_async_operation(name: str) -> None:
    for char in name:
        yield f"{char} from args come"

def run_async_operations() -> None:
    tasks = [
        async_operation("Operation 1", 2),
        async_operation("Operation 2", 3),
        another_async_operation("A B O B A")
    ]
    while tasks:
        for i, task in enumerate(tasks):
            try:
                print(next(task))
            except StopIteration:
                print(f"Operation {i} is completed!")
                tasks.pop(i)

if __name__ == "__main__":
    run_async_operations()
