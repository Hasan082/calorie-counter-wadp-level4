# Calorie Counter Web Application

## Overview
Calorie Counter is a professional Django-based web application designed to help users track their daily calorie intake and monitor their Basal Metabolic Rate (BMR). The platform provides a user-friendly dashboard, profile management, and calorie entry features, making it easy for individuals to manage their dietary goals and maintain a healthy lifestyle.

## Features
- **User Registration & Authentication:** Secure sign-up, login, and logout functionality using Django's built-in authentication system.
- **Profile Management:** Users can create and update their profile, including gender, age, weight, and height. The system automatically calculates and updates the user's BMR based on profile data.
- **Dashboard:** A visually appealing dashboard displays:
  - Required daily calories (BMR)
  - Calories consumed today
  - Recent meal entries
  - Quick access to profile and calorie entry pages
- **Calorie Entry:** Users can log meals with item names, dates, and calorie values. The dashboard aggregates and displays daily totals and recent entries.
- **Responsive Design:** Modern, mobile-friendly UI using Bootstrap 5 and custom CSS for a seamless experience across devices.
- **Alerts & Feedback:** Success and error messages guide users through registration, login, profile updates, and calorie entries.

## How It Works
1. **Register & Login:** Users create an account and log in to access personalized features.
2. **Set Up Profile:** Users enter their personal details. The app calculates BMR using the Harris-Benedict equation.
3. **Add Calorie Entries:** Users log meals and calories consumed each day.
4. **View Dashboard:** The dashboard summarizes BMR, calories consumed, and recent meals. Users can quickly navigate to add new entries or update their profile.
5. **Logout:** Securely log out from any page.

## Technology Stack
- **Backend:** Django 5
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **Database:** SQLite (default, can be swapped for PostgreSQL/MySQL)

## Functionality Summary
- One-to-one user profile with BMR calculation
- Calorie entry and daily aggregation
- Recent meals listing
- Profile and calorie management via modern UI
- Secure authentication and session management

## Getting Started
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd calorie-counter-wadp-level4
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```
5. Access the app at `http://127.0.0.1:8000/`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
