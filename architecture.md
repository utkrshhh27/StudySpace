# StudySpace — System Architecture

## 1. Architecture Overview

StudySpace will use a modular monolithic architecture. The application will have a frontend, a Python Flask backend, and a relational database.

The frontend will display information and collect user input. The backend will validate requests, apply booking rules, check permissions, and communicate with the database.

## 2. Main Components

### 2.1 Frontend

Planned technologies: HTML, CSS, JavaScript, and Bootstrap.

Responsibilities:
- Display the login page.
- Show campus buildings and available spaces.
- Provide search and filter options.
- Display booking details and reservation status.
- Provide suitable dashboards for users and administrators.

### 2.2 Backend

Planned technology: Python Flask.

Responsibilities:
- Process requests from the frontend.
- Validate user input.
- Check user permissions.
- Check room availability before confirming bookings.
- Create, retrieve, and cancel eligible reservations.
- Provide data for utilization reports.

### 2.3 Database

Planned technology: Azure SQL Database, subject to subscription availability and cost.

The database will store:
- Users and roles.
- Buildings and spaces.
- Facilities available in each space.
- Existing scheduled events.
- Booking requests and reservations.
- Booking status history and relevant activity logs.

### 2.4 Cloud File Storage

Planned service: Azure Blob Storage, if available and required.

It may store room photographs or other approved project files. The database will store references to these files rather than the files themselves.

## 3. Basic Data Flow

1. A user opens the StudySpace website.
2. The frontend sends a request to the Flask backend.
3. The backend validates the request and checks the user's permissions.
4. The backend retrieves or updates the relevant database records.
5. The database returns the result.
6. The backend sends a response to the frontend.
7. The frontend displays the result to the user.

## 4. Booking Workflow

1. The user selects a building, room, date, and time.
2. The backend checks existing schedules and active reservations.
3. If the requested slot is unavailable, the system informs the user.
4. If the slot is available, the system applies the relevant booking and approval rules.
5. The database transaction rechecks availability and saves the reservation safely.
6. The user sees the resulting status, such as confirmed or pending approval.

The system must handle simultaneous requests safely so that two overlapping reservations cannot both be confirmed.

## 5. Proposed API Design

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /api/auth/login | Log in a user |
| GET | /api/buildings | List campus buildings |
| GET | /api/spaces | Search and filter spaces |
| GET | /api/spaces/availability | Check room availability |
| POST | /api/bookings | Submit a booking request |
| GET | /api/bookings/my | View the current user's bookings |
| PATCH | /api/bookings/{id}/cancel | Cancel an eligible booking |
| POST | /api/admin/spaces | Add a space |
| GET | /api/admin/analytics | Retrieve utilization statistics |

These endpoints are proposed designs and will be refined during implementation.

## 6. Security Design

- Use secure authentication and role-based authorization.
- Verify permissions on the backend for every protected operation.
- Use parameterized SQL queries.
- Store passwords as secure hashes rather than plain text.
- Use HTTPS in deployment.
- Keep database credentials and other secrets out of source control.
- Restrict database access through appropriate network and firewall settings.

## 7. Scaling and Performance

The initial project will use a modular monolith instead of microservices because it is simpler to develop, test, and deploy as a solo project.

Database indexes will be considered for frequently searched fields, such as space identifiers, building identifiers, booking status, and time ranges. Search results can use pagination if the dataset grows.

Caching will not be introduced initially because room availability changes frequently and stale information could cause booking problems.

## 8. Planned Deployment

The application will be deployed using an eligible cloud hosting service after subscription access, security, and cost have been checked.

The deployed frontend will communicate with the backend over HTTPS, and the backend will access the database using protected credentials.

## 9. Architecture Status

This document describes the planned architecture. The actual implementation and final cloud services may change after project approval and technical testing.