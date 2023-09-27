## **Project Summary: Club Event Management System**

The Club Event Management System is a web application that allows users to manage and view events organized by various clubs. The system is built using Flask (a Python web framework) and a SQL Server database to store event-related data. The project provides various APIs for retrieving, creating, and updating events, clubs, and user information.

**Features:**

1. **Events API:** Allows users to view all events, fetch event details, and create new events. Event details include the event name, type, day, date, start time, end time, venue, email contact, phone number, budget, ticket information, and event picture.

2. **Clubs API:** Provides information about all clubs, including their names, types, faculty coordinators, email contacts, activities, total events, and photos viewer link.

3. **User API:** Manages different types of users, including student members, faculty members, and student welfare members. Users are associated with specific clubs.

4. **Event Approval System:** Events can have different statuses like 'Pending', 'Approved', or 'Denied'. Events are displayed until the event date. After the event date, they are moved to past events.

5. **Event Creation API:** Allows authorized users to create new events by providing necessary details, including pictures and URLs.

**Database Structure:**

The project uses a SQL Server database with the following tables:
- Events: Contains event-related information, including the new columns Event_Status and Event_Details.
- Clubs: Stores club-related data.
- User_Student, User_Faculty, and User_Student_Welfare: Store information about different types of users and their association with clubs.

**Conclusion:**

The Club Event Management System provides a robust platform for managing and organizing events for various clubs. With its API-based architecture, it can be easily extended and integrated with other applications. The project offers flexibility, scalability, and efficiency in managing club events, making it a valuable tool for event organizers.

Figma: https://www.figma.com/file/wmOX51bN9Lz3rfEdLczTo7/NEW-FIGMA-LEAD-FINAL?type=design&node-id=0-1&mode=design
