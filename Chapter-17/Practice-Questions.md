# Solutions for the Practice Questions in Chapter 17

## 1. What is the Unix epoch?
The moment from which programs calculate the current date and time. (UTC January 1st, 1970)
## 2. What function returns the number of seconds since the Unix epoch?
time.time()
## 3. How can you pause your program for exactly 5 seconds?
time.sleep(5)
## 4. What does the round() function return?
It rounds the given float to the nearest integer
## 5. What is the difference between a datetime object and a timedelta object?
A datetime object represents a moment in time. A timedelta object represents duration.
## 6. Using the datetime module, what day of the week was January 7, 2019?
Monday
## 7. Say you have a function named spam(). How can you call this function and run the code inside it in a separate thread?
```
threadObj = threading.Thread(target=spam)
threadObj.start()
```
## 8. What should you do to avoid concurrency issues with multiple threads?
We should make sure that all variables in different threads are distinct.