# court_dashboard
### 🏛 Court Chosen  
Delhi High Court – [https://delhihighcourt.nic.in/app/get-case-type-status](https://delhihighcourt.nic.in/app/get-case-type-status)

### Simple Setup  
Run these commands:  
'python manage.py makemigrations'
'python manage.py migrate'
'python manage.py runserver'

### CAPTCHA Strategy  
Manual CAPTCHA – the script waits 15 seconds for user to enter CAPTCHA on the website.

### Sample Env Vars  
env
SECRET_KEY=your_secret_key
DEBUG=True
