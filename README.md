# remote-nanny





heroku is awesome!

Development
0. heroku git:remote -a on-demand-nanny (app name in heroku, do this only once to register this)
1. make changes
2. git add and git commit
3. ENV = "dev" for local setup, update the postgres URL to your local machine
4. git push heroku master
5. heroku pg:psql --app on-demand-nanny (connect to the database)
6. heroku run python (for shell access!)
