# todoapp
a simple to do app with django as backend and nextjs as frontend
Project Setup Instructions
This project utilizes both Django and Next.js frameworks. Follow the steps below to set up the project after cloning or pulling it from the repository:

Install Django Dependencies:

Navigate to the project directory (todoapp).
create a virtual environment, activate it.
Run the following command to install Python dependencies:


cd todoapp  #to change directory to the project directory
pip install -r requirements.txt


Install Next.js Dependencies:

Navigate to the nextjs project directory  (frontend).
cd frontend  # to change directory to the project directory

**install next.js dependency**
Run either of the following commands to install JavaScript dependencies:
npm install # to install dependency


**Start Django Server:**

Once Django dependencies are installed, start the Django development server:

# enter the following command on the terminal
python manage.py runserver


**Start Next.js Development Server:**

After installing Next.js dependencies, start the Next.js development server:

# enter the following command on the terminal
cd frontend
npm run dev

**Access the Application:**

Once both Django and Next.js servers are running, you can access the application in your web browser.
Django server typically runs on http://localhost:8000.
Next.js server typically runs on http://localhost:3000.
