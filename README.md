Live demo: https://employee-management-plfs.onrender.com

# Employee Management System

A modern, responsive Django web application for managing employee records with a beautiful UI/UX design.

## Features

- **View Employees**: Display all employees in a clean, responsive table
- **Add Employees**: User-friendly form with dropdown selections for departments and roles
- **Update Employees**: Edit existing employee information
- **Remove Employees**: Delete employees with confirmation prompts
- **Filter Employees**: Search and filter employees by name, department, or role
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Built with Bootstrap 5 and Font Awesome icons

## Technologies Used

- **Backend**: Django 5.1
- **Frontend**: HTML5, CSS3, Bootstrap 5, Font Awesome
- **Database**: SQLite
- **Styling**: Custom CSS with responsive design

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vanshchoudhary78/Employee-Management.git
   cd Employee-Management/office_emp_proj
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Populate sample data (optional):
   ```bash
   python populate_data.py
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

- **Home**: Overview of the system with navigation to all features
- **View Employees**: See all employees in a table format with action buttons
- **Add Employee**: Fill out the form to add new employees
- **Update Employee**: Select an employee from the list and modify their details
- **Remove Employee**: Choose employees to delete with confirmation
- **Filter Employees**: Use search criteria to find specific employees

## Screenshots

The application features:
- Clean navigation bar with all main functions
- Card-based layouts for better visual hierarchy
- Responsive tables with hover effects
- Form validation and user feedback
- Confirmation dialogs for destructive actions
- Mobile-friendly design

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).

---
