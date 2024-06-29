# TaskTrekker App

#### Video Demo:
https://youtu.be/5UkTxUEsmUU

#### Description:
TaskTrekker is a robust task management web application built using Python and the Flask framework. It provides users with a convenient way to organize and track tasks across multiple lists, enhancing productivity and efficiency in personal and professional environments.

TaskTrekker allows users to create tasks with detailed descriptions and due dates, edit task details as needed, mark tasks as completed, and manage multiple task lists simultaneously. The application's intuitive interface and flexible features make it suitable for various organizational needs, from simple to-do lists to complex project management.

Project Structure and Files:
main.py: This file serves as the entry point for the TaskTrekker application. It initializes the Flask app, defines routes for handling different HTTP requests, and integrates with the application's core functionality.

templates/: This directory contains HTML templates used to render the user interface of TaskTrekker. Each template corresponds to a specific page or functionality within the application, providing a structured layout and interaction points for users.

static/: Here, you'll find static assets such as CSS stylesheets, JavaScript files, and images used to enhance the visual presentation and functionality of TaskTrekker. These resources ensure a consistent and appealing user experience across different devices and browsers.

app.py: This file encapsulates the application logic, including functions for task creation, editing, deletion, marking tasks as completed, and managing task lists. It interacts with the Flask framework to handle user requests, validate input data, and update the application's state accordingly.

models.py: Defines the data models used by TaskTrekker, such as the Task and TaskList classes. These models encapsulate task-related attributes (e.g., description, due date, completion status) and provide methods for interacting with tasks and task lists in the database.

forms.py: Manages web forms used for user input and validation within TaskTrekker. It integrates with Flask-WTF (WTForms) to define form fields, handle form submissions, and validate user-provided data before processing it further in the application.

Design Choices:
TaskTrekker was designed with usability and flexibility in mind, focusing on the following key principles:

Simplicity and Intuitiveness: The user interface is straightforward and user-friendly, allowing users to quickly grasp how to create, edit, and manage tasks without unnecessary complexity.

Flexibility in Task Management: Supporting multiple task lists and sorting options (by name, due status, due date) ensures that users can adapt TaskTrekker to their unique organizational needs, whether managing personal tasks or coordinating team projects.

Responsive Design: By leveraging Bootstrap for CSS styling and responsive layout, TaskTrekker provides a seamless experience across desktop and mobile devices, accommodating different screen sizes and resolutions.

Data Integrity and Security: Utilizing Flask-SQLAlchemy for database management ensures robust data handling and persistence, while incorporating best practices for data validation and user authentication (planned for future updates) enhances overall security.

Usage:
To run TaskTrekker locally on your machine, follow these steps:

1. Clone the repository: git clone https://github.com/your-username/tasktrekker.git
2. Navigate to the project directory: cd tasktrekker
3. Install dependencies: pip install -r requirements.txt
4. Run the application: python main.py
5. Open a web browser and go to http://127.0.0.1:5000 to start using TaskTrekker.

Features:
* Create and Manage Tasks: Create tasks with descriptions and due dates, edit task details, and mark tasks as completed.
* Organize with Multiple Lists: Manage multiple task lists for different projects or categories.
* Sort and Filter: Sort tasks by name, due status, or due date, and view completed tasks within each list.
* Responsive Interface: Designed with Bootstrap for responsive design, ensuring usability across devices.

Future Improvements: 
Planned enhancements include user authentication for secure task management and advanced task categorization and filtering capabilities.

Technologies Used:
* Python: Backend logic and application scripting.
* Flask: Microframework for web development in Python.
* Flask-SQLAlchemy: Database management using SQLAlchemy with Flask integration.
* Bootstrap: CSS framework for responsive design and styling.
* HTML/CSS/JavaScript: Frontend development for user interface and interactivity.

Acknowledgments:
* Bootstrap: CSS framework for styling.
* Flask: Python web framework.
* SQLAlchemy: Python SQL toolkit and Object-Relational Mapping (ORM) library.
