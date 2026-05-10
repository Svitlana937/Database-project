# Conference Management System

A comprehensive database-driven application for managing conference attendees, sessions, speakers, and networking connections using both relational (MySQL) and graph (Neo4j) databases.

## 🌟 Features

### Core Functionality
- **Speaker & Session Search**: Find speakers and their scheduled sessions by name
- **Company Attendee Management**: View all attendees from a specific company with their session registrations
- **Attendee Registration**: Add new attendees to the conference database
- **Networking Connections**: View and create connections between attendees using graph database
- **Room Management**: Display conference rooms with capacity information

### Database Architecture
- **MySQL**: Handles relational data (attendees, companies, sessions, rooms, registrations)
- **Neo4j**: Manages attendee networking relationships and connections

## 🛠️ Technologies Used

- **Python 3.x**
- **MySQL** - Relational database for structured data
- **Neo4j** - Graph database for attendee relationships
- **mysql-connector-python** - MySQL database connector
- **neo4j-driver** - Neo4j Python driver

## 📋 Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.7+
- MySQL Server
- Neo4j Desktop/Server
- Required Python packages (see Installation)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Svitlana937/Database-project.git
cd Database-project
```

### 2. Install Dependencies
```bash
pip install mysql-connector-python neo4j
```

### 3. Database Setup

#### MySQL Setup
1. Create a MySQL database named `conference_db`
2. Update connection details in `config_db.py` if needed:
   ```python
   db = mysql.connector.connect(
       host="localhost",
       user="your_username",
       password="your_password",
       database="conference_db"
   )
   ```

#### Neo4j Setup
1. Start your Neo4j instance
2. Update connection details in `config_neo4j.py` if needed:
   ```python
   uri = "bolt://localhost:7687"
   user = "neo4j"
   password = "your_password"
   ```

### 4. Database Schema

The application expects the following MySQL tables:

- `attendee` (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
- `company` (companyID, companyName)
- `session` (sessionID, sessionTitle, speakerName, sessionDate, roomID)
- `room` (roomID, roomName, capacity)
- `registration` (attendeeID, sessionID)

## 🎯 Usage

Run the application:
```bash
python main.py
```

### Menu Options

1. **View Speakers & Sessions**
   - Search for speakers by name
   - Displays speaker name, session title, and room

2. **View Attendees by Company**
   - Enter company ID to view all attendees
   - Shows attendee details and their registered sessions

3. **Add New Attendee**
   - Register new conference attendees
   - Validates attendee ID, gender, and company existence

4. **View Connected Attendees**
   - Display networking connections for an attendee
   - Uses Neo4j graph database for relationships

5. **Add Attendee Connection**
   - Create networking connections between attendees
   - Prevents duplicate connections

6. **View Rooms**
   - Display all conference rooms with capacity

## 🏗️ Project Structure

```
Database-project/
├── main.py              # Application entry point and menu logic
├── interface.py         # User interface and menu display
├── db_queries.py        # Database operations for MySQL and Neo4j
├── config_db.py         # MySQL database configuration
├── config_neo4j.py      # Neo4j database configuration
├── validators.py        # Input validation functions
└── README.md           # Project documentation
```

## 🔧 Configuration

### Database Connections

**MySQL Configuration** (`config_db.py`):
- Host: localhost (default)
- User: root (default)
- Password: root (default)
- Database: conference_db

**Neo4j Configuration** (`config_neo4j.py`):
- URI: bolt://localhost:7687
- User: neo4j
- Password: password

## 📊 Data Flow

1. **Relational Data (MySQL)**:
   - Attendee information and demographics
   - Company details
   - Session schedules and speaker information
   - Room details and capacities
   - Registration records

2. **Graph Data (Neo4j)**:
   - Attendee networking relationships
   - Social connections between conference participants

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Known Issues

- Some code contains duplicate conditional statements that should be cleaned up
- Error handling could be improved in database operations
- Input validation could be more comprehensive

## 📞 Support

For questions or issues, please open an issue on the GitHub repository.

---

**Built with ❤️ for efficient conference management**