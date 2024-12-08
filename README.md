Ideana rakentaa AI apuri tietokantoihin ja opintojen tuelle.
Tässä suunnitelma projektille / Here is the roadmap for the project. Built (8.12) and will be updated as I progress!


High-Level Overview of the AI Assistant Project

1. Goal is to create an AI-powered assistant that helps users with task management and provides additional intelligent features.

2. Core Features:
   - Task management: Users can create, view, edit, and delete tasks.
   - AI integration: ChatGPT-like assistant for answering questions or helping users organize their work.
   - User authentication: Each user has their own account and can manage personal tasks.
   - Notifications and reminders: Notify users of due tasks or events.

3. Tech Stack:
   - Backend: Django (Python framework)
   - Database: SQLite (development) or PostgreSQL (production)
   - Frontend: Basic templates with Django or advanced UI with React.js
   - AI Integration: OpenAI API or a custom-trained machine learning model
   - Environment: Python, virtual environments, and GitHub for version control


What I have Accomplished so far (7.12)

1. Set Up the Project:
   - Installed Python, Django, and created a virtual environment.
   - Initialized a Django project named "ai_assistant".
   - Pushed your code to GitHub for version control.

2. Configured the Development Environment:
   - Verified Django installation.
   - Created a superuser for the Django admin panel.
   - Configured and tested the development server to ensure it runs properly.

3. Started the Task Management App:
   - Created an app called "projects" for managing tasks.
   - Defined a `Project` model and migrated it to the database.
   - Registered the model with Django admin.

Detailed Roadmap

Phase 1: Foundation (Complete) (7.12)

- Tools Used:
  - Django: Framework for building the backend.
  - SQLite: Default database for local development.
  - PyCharm: IDE for Python development.
  - Git/GitHub: For version control and collaboration.

Steps Completed:
1. Installed Django and initialized the project.
2. Set up a working virtual environment.
3. Created the basic app structure (e.g., `projects` app).
4. Defined a database schema for `Project` and migrated it.
5. Tested the server to ensure the project runs locally.
6. Successfully pushed code to GitHub.



Phase 2: Core Functionality – Task Management

Objective: 
Building a feature-rich task management system with CRUD (Create, Read, Update, Delete) operations.

Steps:

1. Define a `Task` Model:
   - Add fields like title, description, completed status, and timestamps.
   - Create and run migrations to apply changes to the database.

2. Build Views for Task Management:
   - List view: Show all tasks in a table or list format.
   - Detail view: Show details for a single task.
   - Create view: Allow users to create tasks via a form.
   - Edit view: Allow users to update existing tasks.
   - Delete view: Allow users to delete tasks.

3. Create Templates for the Views:
   - Use Django’s templating system to display tasks.
   - Use HTML and Bootstrap to make the interface look clean and user-friendly.

4. Integrate URLs:
   - Add appropriate URL patterns for task-related actions.

5. Test the Features:
   - Ensure tasks can be added, viewed, edited, and deleted without errors.
   - Use Django admin to verify the database content.


Phase 3: User Authentication and Authorization

Objective:
Securing the system by allowing users to manage only their own tasks.

Steps to Follow:

1. Enabling built-in authentication system:
   - Add user registration and login/logout functionality.
   - Use Django’s `User` model to associate tasks with specific users.
   
2. Adding role-based permissions:
   - Ensure only the task owner can edit or delete tasks.
   - Use decorators like `@login_required` to restrict access to authenticated users.

3. Modify task views to show only the logged-in user’s tasks.



Phase 4: AI Integration

Objective:
Adding an AI-powered assistant that provides intelligent recommendations or assistance.

Steps:

1. Choose the AI Service:
   - Use the **OpenAI API** for a ChatGPT-like assistant.
   - Alternatively, use a pre-trained model like Hugging Face's transformers library.

2. Create a Chatbot Interface:
   - Build a simple form where users can ask questions or request assistance.
   - Send queries to the AI service and display responses.

3. Integrate with Tasks:
   - Allow the AI to provide task suggestions or summarize overdue tasks.
   - Example: “You have 3 overdue tasks. Would you like to reschedule them?”

---

Phase 5: Advanced Features

Objective: 
Adding quality-of-life improvements to the app.

Steps:

1. Notifications and Reminders:
   - Use Django Q or Celery to schedule background tasks.
   - Send email or push notifications for upcoming or overdue tasks.

2. Search and Filters:
   - Add a search bar to filter tasks by title or description.
   - Add filters for completed and incomplete tasks.

3. Improved Frontend:
   - Replace basic templates with a React.js frontend for a more dynamic user experience.
   - Use REST framework (Django REST Framework) to build an API for the frontend.

4. Deploy the App:
   - Choose a hosting provider like Heroku or AWS for deployment.
   - Switch to PostgreSQL for production.



Timeline

Phase                     	 Estimated Time 
Foundation	Complete
Task management	2-3 days
User authentication	2-3 days
AI integration	3-4 days
Advanced features	4+  days
Deployment	1-2 days


Next?

Task management feature! :)

1. Finalizing the `Task` model and migrating it.
2. Creating views and templates for CRUD operations.
3. Testing the functionality through Django admin and the browser.
   
