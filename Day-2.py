#Function that takes a list and returns only the even numbers from that list
def filter_even_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers
#Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_even_numbers(numbers))  

#Class Student with properties name,age,grade and a method to display student details
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
#Example usage
student1 = Student("Alice", 20, "A")
print(student1.display_details())

#Dictionary of 5 students and print names of students who scored more than 80
students_scores = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David ": 67,
    "Eva": 88
}
high_scorers = [name for name, score in students_scores.items() if score > 80]
print("Students who scored more than 80:", high_scorers)

#Read a text file and count the number of words in it
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."
#Example usage
file_path = 'sample.txt'  # Make sure to have a sample.txt file in the same directory
print("Number of words in the file:", count_words_in_file(file_path))

#Function to fetch data from a public API and print the response
import requests
def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
#Example usage
api_url = 'https://jsonplaceholder.typicode.com/posts/1'
print("API Response:", fetch_data_from_api(api_url))
