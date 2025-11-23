#Basic Calculator
class calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."
# Example usage:
calc = calculator()
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5)) 
print("Multiplication:", calc.multiply(10, 5))  
print("Division:", calc.divide(10, 5))  
print("Division by zero:", calc.divide(10, 0))

# Simple To-Do List
class ToDoList: 
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f'Task "{task}" added.'

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return f'Task "{task}" removed.'
        else:
            return f'Task "{task}" not found.'

    def view_tasks(self):
        return self.tasks
# Example usage:
todo = ToDoList()       
print(todo.add_task("Buy groceries"))
print(todo.add_task("Read a book"))
print("Current Tasks:", todo.view_tasks())
print(todo.remove_task("Buy groceries"))

print("Current Tasks after removal:", todo.view_tasks())

#JSON File Handling
import json
def write_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    return f'Data written to {file_path}'
def read_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data
# Example usage:   
data_to_write = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
file_path = 'data.json'
print(write_json(file_path, data_to_write))
print("Data read from JSON file:", read_json(file_path))

