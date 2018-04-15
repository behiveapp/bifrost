install:
	docker-compose build
start: 
	docker-compose up
start-debug: 
	docker-compose up -d
	docker attach bifrost
mass-insert:
	docker-compose run app src/script/mass-insert.py
console:
	docker-compose run app -ti