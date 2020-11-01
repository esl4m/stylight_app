# Stylight budget notify app

## To run the app on docker:
- Clone the repo to your local
- cd into folder.
- Create .env file ---> You can copy .env.example then rename and edit it.
- Run the following command `docker-compose up --build -d`
- To check the status of the running containers, run the following command `docker ps -a`
- To get inside the "web" docker container using this: `docker exec -u 0 -it Container_ID bash`

- To create super user inside docker `./manage.py createsuperuser`

- Make migrations: `./manage.py makemigrations` 
- Migrate: `./manage.py migrate`

- Run the server like that: `./manage.py runserver` or restart the "web" container.

To run or insert the data first time:
`./manage.py loaddata budget_notify/fixtures/intial_data.json`


### Application using: 
- Database: mysql 5.7
- Django: 3.1.2

### Questions:
- Task total estimate time:
`4 hours`

- Does your solution avoid sending duplicate notifications?
`Yes`

- How does your solution handle a budget change after a notification has already been sent?
`Script checks all the shops, not only the online shops`
