To create postgresql database:
1. run python
2. from app import db
3. db.create_all()
4. exit()


To creat heroku database:
1. git init
2. heroku login
3. heroku create teslafeedback
4. heroku addons:create heroku-postgresql:hobby-dev --app teslafeedback-testing
5. heroku config --app teslafeedback-testing
6. heroku run python
7. from app import db
8. db.create_all()
9. exit()


To output project requirements:
pipenv lock -r > requirements.txt


git commands:
git add . && git commit -m 'Initial deploy'
heroku git:remote -a teslafeedback-testing
git push heroku master

access heroku database:
heroku pg:psql --app teslafeedback-testing
select * from feedback;

