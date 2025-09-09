# AI Assistant - Project Management System

A modern Django-based project management application with task tracking capabilities.

## Features

- **Project Management**: Create, edit, and delete projects with detailed information
- **Task Tracking**: Add tasks to projects with priority levels and due dates
- **User Management**: Assign tasks to users and track project ownership
- **Search & Filtering**: Find projects and tasks quickly with advanced filtering
- **Progress Tracking**: Visual progress bars and completion statistics
- **Responsive Design**: Modern UI that works on all devices
- **Admin Interface**: Comprehensive admin panel for data management

## Technology Stack

- **Backend**: Django 5.1.4
- **Frontend**: Bootstrap 5.3, HTML5, CSS3
- **Database**: SQLite (configurable for PostgreSQL/MySQL)
- **API**: Django REST Framework
- **Authentication**: Django's built-in authentication system

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
API_KEY=your-api-key-here
```

### Database Configuration

The application uses SQLite by default. To use PostgreSQL or MySQL:

1. Install the appropriate database driver:
   ```bash
   # For PostgreSQL
   pip install psycopg2-binary
   
   # For MySQL
   pip install mysqlclient
   ```

2. Update your `.env` file:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   # or
   DATABASE_URL=mysql://user:password@localhost:3306/dbname
   ```

## Usage

### Creating Projects

1. Navigate to the main page
2. Click "Add New Project"
3. Fill in the project details:
   - Name (required)
   - Description (required)
   - Start date (defaults to today)
   - End date (optional)
   - Completion status

### Managing Tasks

1. Open a project by clicking on its name
2. Click "Add Task" to create new tasks
3. Set task details:
   - Title (required)
   - Description (optional)
   - Priority level (Low, Medium, High, Urgent)
   - Due date (optional)
   - Assigned user (optional)

### Search and Filter

- Use the search bar to find projects by name or description
- Filter by completion status (All, Active, Completed)
- Filter by overdue status
- Sort by various criteria

## API Endpoints

The application includes a REST API for programmatic access:

- `GET /api/projects/` - List all projects
- `POST /api/projects/` - Create a new project
- `GET /api/projects/{id}/` - Get project details
- `PUT /api/projects/{id}/` - Update project
- `DELETE /api/projects/{id}/` - Delete project

Similar endpoints are available for tasks at `/api/tasks/`.

## Development

### Code Quality

The project includes several tools for maintaining code quality:

```bash
# Format code with Black
black .

# Sort imports with isort
isort .

# Check for style issues with flake8
flake8 .

# Run tests
pytest
```

### Database Migrations

When making model changes:

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

## Deployment

### Production Settings

For production deployment:

1. Set `DEBUG=False` in your environment
2. Configure a production database
3. Set up static file serving
4. Configure proper security settings
5. Use a production WSGI server like Gunicorn

### Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "ai_assistant.wsgi:application"]
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue in the repository.