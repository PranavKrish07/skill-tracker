#SkillUp - Master Your Growth
SkillUp is a definitive platform for logging, visualizing, and analyzing professional and personal development. It moves beyond simple to-do lists by allowing users to track progress through granular checkpoints and visual mastery indicators.

#🚀 The Vision
In a world of constant learning, "guessing" your progress isn't enough. SkillUp provides a structured environment to turn abstract learning goals into measurable milestones. Built with a focus on user privacy and practical progress tracking.

#🛠️ Tech Stack
Backend: Django (Python)

Database: SQLite3 (Development)

Frontend: HTML5, CSS3 (Custom violet-themed UI), JavaScript

Production Readiness: Configured with WhiteNoise for static file management

✨ Key Features
Secure User Authentication: Full signup and login system where users' data is strictly isolated to their own accounts.

Dynamic Skill Management: Create, track, and delete skills through a clean, intuitive dashboard.

Granular Checkpoints: Each skill can have multiple "checkpoints." Progress is calculated in real-time as these are completed.

Interactive Progress Visualization: Features a live progress bar that reflects mastery levels using custom CSS animations.

Bulk Updates: Uses Django ModelFormSet to allow users to update multiple checkpoint statuses simultaneously, improving efficiency.

🏗️ Technical Highlights
Data Isolation
The app uses a strict ForeignKey relationship between the User model and the Skill model. This ensures that when a user logs in, the view filters only the skills associated with that specific session:

Python

skills = Skill.objects.filter(user=request.user)
Advanced Form Handling
Instead of standard forms, SkillUp utilizes modelformset_factory to manage the collection of checkpoints. This allows for the seamless handling of multiple boolean fields (completed/not completed) in a single POST request.

🚦 Getting Started
Prerequisites
Python 3.x

Django 5.2.6

Installation
Clone the repository:

Bash

git clone https://github.com/pranavkrish07/skill-tracker.git
cd skill-tracker
Install dependencies:

Bash

pip install -r requirements.txt
Run Migrations:

Bash

python manage.py migrate
Start the Server:

Bash

python manage.py runserver
Access the app at http://127.0.0.1:8000/

🔮 Future Roadmap
Two-Factor Authentication (2FA): Implementing enhanced security for user data.

GitHub API Integration: Automatically syncing coding activity with skill progress.

Data Analytics: Providing weekly growth charts and learning velocity metrics.

Developed by Pranav Krishna Aspiring Product Founder | CS Student | Web Developer
