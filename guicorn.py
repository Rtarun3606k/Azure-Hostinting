# guicorn.py

bind = "0.0.0.0:8000"
workers = 2
threads = 4
timeout = 120


# Run the app using the command below:

# gunicorn -c guicorn.py app:app