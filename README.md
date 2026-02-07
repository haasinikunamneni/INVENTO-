# Invento - Inventory Management System

A comprehensive desktop-based Inventory Management System built with Python and Tkinter, designed for efficient management of products, suppliers, categories, employees, and sales.

## 📋 Table of Contents
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Credits](#credits)

## ✨ Features

### User Authentication
- Secure login and signup system
- User credentials stored in `datasheet.txt`
- Password-protected access to the system

### Dashboard
- Real-time clock display
- Overview of total employees, suppliers, categories, products, and sales
- Color-coded information panels for quick insights
- Easy navigation menu

### Employee Management
- Add, update, and delete employee records
- Search functionality by multiple criteria
- Store employee details including contact information and salary

### Supplier Management
- Manage supplier information with invoice tracking
- Add supplier descriptions
- Search and filter supplier records
- Update and delete supplier entries

### Category Management
- Create and manage product categories
- Delete existing categories
- View all categories in a structured table

### Product Management
- Comprehensive product information management
- Link products to categories and suppliers
- Track product prices and quantities
- Monitor product status (Active/Inactive)
- Advanced search and filter options

### Sales Management
- View and search customer bills
- Bill storage in text format
- Invoice number-based retrieval
- Customer bill area for easy viewing

## 🖥️ System Requirements

- Python 3.x
- Operating System: Windows, macOS, or Linux
- Screen Resolution: Minimum 1350x700

## 📦 Installation

1. **Clone or Download the Repository**
   ```bash
   git clone <repository-url>
   cd invento
   ```

2. **Install Required Dependencies**
   ```bash
   pip install tkinter
   ```
   Note: Tkinter usually comes pre-installed with Python

3. **Set Up the Database**
   - The application uses SQLite database (`ims.db`)
   - Database tables will be created automatically on first run
   - Required tables: `employee`, `supplier`, `category`, `product`

4. **Prepare Required Files**
   - Create a `bill` folder in the project directory for storing sales bills
   - Ensure `login.png` and `login1.png` images are in the project directory
   - The `datasheet.txt` file will be created automatically for user authentication

## 🚀 Usage

1. **Start the Application**
   ```bash
   python trial__1_.py
   ```

2. **First Time Setup**
   - Click "Sign up" to create a new account
   - Enter username and password
   - Confirm password and complete registration

3. **Login**
   - Enter your username and password
   - Click "Sign in" to access the dashboard

4. **Navigate the System**
   - Use the left menu to access different modules:
     - Employee
     - Supplier
     - Category
     - Product
     - Sales
   - Click "Logout" to return to the login screen
   - Click "Exit" to close the application

## 📁 Project Structure

```
invento/
│
├── trial__1_.py          # Main application file with login and dashboard
├── employee.py           # Employee management module
├── supplier.py           # Supplier management module
├── category.py           # Category management module
├── product.py            # Product management module
├── sales.py              # Sales management module
│
├── ims.db                # SQLite database (auto-generated)
├── datasheet.txt         # User credentials storage (auto-generated)
│
├── bill/                 # Directory for storing sales bills
├── login.png             # Login screen background image
├── login1.png            # Signup screen background image
│
└── README.md             # This file
```

## 🗃️ Database Schema

### Employee Table
- Employee ID (Primary Key)
- Name
- Email
- Gender
- Contact
- Date of Birth (DOB)
- Date of Joining (DOJ)
- Password
- User Type
- Address
- Salary

### Supplier Table
- Invoice (Primary Key)
- Name
- Contact
- Description

### Category Table
- Category ID (Primary Key)
- Category Name

### Product Table
- Product ID (Primary Key)
- Category
- Supplier
- Name
- Price
- Quantity
- Status

## 🎨 Color Scheme

- Primary Background: `#edcbd2` (Light Pink)
- Header: `#e3856b` (Coral)
- Buttons: `#80c4b7` (Teal)
- Accent Colors:
  - Red: `#ff0000` (Employee)
  - Blue: `#0000ff` (Supplier)
  - Green: `#00ff00` (Category)
  - Purple: `#a020f0` (Product)
  - Black: `#000000` (Sales)

## 🔧 Key Functions

### Authentication System
- `signin()` - Validates user credentials
- `signup()` - Creates new user accounts
- `logout()` - Returns to login screen

### CRUD Operations
All modules support:
- **Create**: Add new records
- **Read**: View all records in table format
- **Update**: Modify existing records
- **Delete**: Remove records with confirmation
- **Search**: Filter records by various criteria

## ⚠️ Important Notes

1. **Database Connection**: The system uses SQLite with the database file `ims.db`. Ensure proper file permissions.

2. **Bill Storage**: Sales bills are stored as `.txt` files in the `bill/` directory. Create this folder before using the sales module.

3. **Image Files**: The login screens require `login.png` and `login1.png`. Place these in the project root directory.

4. **Security**: User passwords are stored in plain text in `datasheet.txt`. For production use, implement proper password hashing.

## 🐛 Known Issues

1. Supplier module has incorrect column indexing in `get_data()` method
2. No password encryption in the authentication system
3. SQL injection vulnerability in search functions (use parameterized queries)

## 🔮 Future Enhancements

- Implement password hashing for security
- Add data validation for all input fields
- Create backup and restore functionality
- Generate PDF reports for sales and inventory
- Add user role-based access control
- Implement email notifications
- Add data export to Excel/CSV

## 👥 Credits

**Developed by:** XII-B Class Project Team
- Haasini
- Kushal

## 📄 License

This project is created as an educational project. Feel free to use and modify as needed.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

---

**Note:** This is a school project developed for learning purposes. For production use, additional security measures and code improvements are recommended.
