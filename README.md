# Django Todo App

This Django Todo App is a simple yet powerful tool for managing your daily tasks. Built using Django, a high-level Python web framework, this application provides an intuitive interface for users to create, update, and delete their todos effortlessly.

## Features
- **Create Todos**: Users can easily create new todos with titles and descriptions to keep track of their tasks.
- **Update Todos**: Edit and modify existing todos to reflect changes or progress.
- **Delete Todos**: Remove completed or irrelevant todos from the list.
- **Mark Todos as Completed**: Keep track of completed tasks by marking todos as done.

### Installation

```python

#Clone the repository to your local machine
git clone https://github.com/voidmain69/py-todo-list.git
  
#Navigate to the project directory:
cd project-directory

#Set up and activate a virtual environment (optional but recommended):
python3 -m venv venvsource venv/bin/activate

#Install Django and other dependencies:
pip install -r requirements.txt

#Set up the database:
python manage.py migrate
    
#Optionally, you can load demo data for testing purposes:
python manage.py loaddata initial_data.json

#Create a .env file in the project directory and add your environment variables:
SECRET_KEY=your_secret_key
DEBUG=True
    
#Start the Django server:
python manage.py runserver
```

## Usage
1. Once logged in, you'll be directed to the dashboard where you can see your todos.
2. Click on "Add Todo" to create a new todo.
3. Fill in the title and description of the todo and click "Save".
4. Your new todo will appear on the dashboard.
5. To mark a todo as completed, simply click the btn next to it.
6. To edit or delete a todo, click on the todo and select the appropriate action.


### Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

### License

This project is licensed under the MIT License.

### Acknowledgements

This project was inspired by the Kanban methodology and aims to provide a user-friendly tool for project management and collaboration.