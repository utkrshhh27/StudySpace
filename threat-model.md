# StudySpace — Threat Model

## 1. Introduction

This threat model identifies possible security risks in the StudySpace Smart Campus Space Booking and Utilization System.

The purpose is to protect user accounts, booking information, room schedules, and administrative functions from unauthorized access or misuse.

## 2. Important Assets

The main assets that need protection are:

- User account information and password hashes.
- Building, room, and facility information.
- Booking requests and reservation records.
- Existing class and event schedules.
- Administrative functions.
- Database credentials and cloud configuration.
- Activity logs and utilization reports.

## 3. Potential Threats and Mitigations

### Threat 1: Unauthorized Access

Risk: A user may attempt to access administrative functions without permission.

Mitigation:
- Implement secure login.
- Use role-based authorization.
- Check permissions on the backend for every protected action.
- Do not rely only on hiding buttons in the frontend.

### Threat 2: Booking Another User's Reservation

Risk: A user may try to view or modify another user's booking.

Mitigation:
- Verify booking ownership on the backend.
- Allow only authorized administrators to perform approved administrative actions.
- Return only the information needed for each request.

### Threat 3: Overlapping Bookings

Risk: Two users may attempt to reserve the same room for overlapping time periods.

Mitigation:
- Check existing bookings and scheduled events.
- Recheck availability during the database transaction.
- Use suitable database locking or transaction isolation.
- Confirm a reservation only after the availability rules are satisfied.

### Threat 4: SQL Injection

Risk: Malicious input may attempt to change database queries.

Mitigation:
- Use parameterized SQL queries.
- Validate user input on the backend.
- Avoid building SQL statements by directly joining user input into query strings.

### Threat 5: Weak Password Protection

Risk: Poor password handling may expose user accounts.

Mitigation:
- Store passwords using a suitable password-hashing algorithm.
- Never store passwords as plain text.
- Use secure authentication practices and protect login sessions.

### Threat 6: Exposure of Cloud Credentials

Risk: Database passwords or other secrets may accidentally be published in the source-code repository.

Mitigation:
- Store secrets in environment variables or an appropriate cloud secret store.
- Add local secret files to `.gitignore`.
- Never commit real passwords, connection strings, or API keys to GitHub.
- Rotate credentials if they are accidentally exposed.

### Threat 7: Unauthorized Schedule Changes

Risk: An unauthorized user may change existing classes or events, making room availability inaccurate.

Mitigation:
- Restrict schedule-management functions to authorized staff.
- Validate all schedule changes on the backend.
- Record important administrative actions.

### Threat 8: Invalid or Malicious Input

Risk: Invalid dates, incorrect time ranges, or unsafe text may cause errors or security problems.

Mitigation:
- Validate dates and times on the backend.
- Ensure the end time is later than the start time.
- Use database constraints where appropriate.
- Escape user-generated text when displaying it in web pages.

### Threat 9: Unauthorized Database Access

Risk: An attacker may attempt to connect directly to the database.

Mitigation:
- Use appropriate firewall and network access restrictions.
- Keep database credentials private.
- Grant only the permissions required by the application.
- Use encrypted connections where supported.

## 4. Security Measures

The planned security controls include:

- HTTPS for communication in deployment.
- Secure authentication and role-based authorization.
- Password hashing.
- Backend input validation.
- Parameterized SQL queries.
- Protected cloud credentials.
- Appropriate database network restrictions.
- Activity logging for important actions.
- Testing of booking conflicts and access permissions.

## 5. Testing Plan

The following checks will be performed during implementation:

1. Verify that users cannot access restricted administrative functions.
2. Verify that users cannot modify other users' bookings.
3. Test overlapping booking requests.
4. Test invalid dates and time ranges.
5. Check that database credentials are not committed to GitHub.
6. Verify that unauthorized schedule changes are rejected.
7. Test that protected endpoints require appropriate authentication.

## 6. Data Privacy

The development version will use dummy campus and user data. Real student records, personal information, and confidential university schedules will not be used without explicit authorization.

## 7. Conclusion

StudySpace will use layered security controls to protect user accounts, booking records, schedules, and administrative functions. These controls will be implemented and tested during development.

This document describes the planned threat model. Final controls will be verified against the actual application and cloud configuration.