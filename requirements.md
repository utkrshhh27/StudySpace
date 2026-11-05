# StudySpace — Requirements Document

## 1. Project Overview

StudySpace is a Smart Campus Space Booking and Utilization System. It helps students, faculty, and campus staff find and reserve available rooms across different campus buildings.

The system will support study rooms, project rooms, classrooms, laboratories, seminar halls, workshops, and club activities.

## 2. Problem Statement

Finding available rooms across campus buildings can be difficult. Manual booking may cause overlapping reservations, confusion about room availability, and poor tracking of room usage.

StudySpace aims to solve these problems by providing a centralized platform to search for spaces, manage reservations, and analyze room utilization.

## 3. Target Users

- Students: Find and reserve eligible study spaces.
- Faculty: Request rooms for classes and laboratory sessions.
- Campus Staff: Request spaces for workshops, meetings, and university activities.
- Administrators: Manage buildings, spaces, schedules, booking requests, and reports.

## 4. Project Objectives

1. Display available spaces across multiple campus buildings.
2. Make room reservations easier to manage.
3. Prevent overlapping confirmed bookings.
4. Provide authorized management of rooms and schedules.
5. Generate reports to help administrators understand space usage.

## 5. Core Features

1. Search and filter spaces by building, room type, capacity, facilities, date, and time.
2. Allow users to create, view, and cancel eligible reservations.
3. Allow faculty and staff to request spaces for academic and campus activities.
4. Allow administrators to manage rooms, schedules, and booking approvals.
5. Check room availability before confirming a reservation.
6. Generate utilization reports showing popular rooms and peak booking hours.

## 6. Functional Requirements

- FR-01: The system shall provide secure user login.
- FR-02: Users shall be able to browse campus buildings and spaces.
- FR-03: Users shall be able to filter spaces by relevant criteria.
- FR-04: Eligible users shall be able to submit booking requests.
- FR-05: The system shall prevent overlapping confirmed bookings.
- FR-06: Users shall be able to view their reservations.
- FR-07: Users shall be able to cancel eligible reservations.
- FR-08: Authorized administrators shall manage rooms and schedules.
- FR-09: Authorized staff shall review requests requiring approval.
- FR-10: Administrators shall be able to view space utilization reports.

## 7. Non-Functional Requirements

- Security: Protect accounts and restrict actions according to user roles.
- Reliability: Maintain consistent booking records.
- Performance: Return search results within a reasonable time.
- Usability: Provide a simple, easy-to-understand interface.
- Maintainability: Keep the application organized into clear modules.
- Cost Control: Prefer eligible free services, student credits, or university resources.

## 8. Planned Technology Stack

- Frontend: HTML, CSS, JavaScript, Bootstrap
- Backend: Python with Flask
- Database: Azure SQL Database, subject to availability and cost
- File Storage: Azure Blob Storage, if available and required
- Analytics: Power BI or an approved alternative
- Version Control: Git and GitHub

## 9. Project Scope and Limitations

- The first version will use sample campus data.
- Authorized administrators will initially enter existing classes and events.
- Automatic university timetable integration is outside the initial scope.
- Booking permissions and approval rules will follow the project's approved requirements.
- Cloud services will be selected after checking subscription access and costs.

## 10. Expected Outcome

The expected outcome is a working web application that helps students, faculty, and staff discover spaces, manage reservations, and allows administrators to monitor room utilization across campus buildings.