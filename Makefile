 upbuild: up build

 up:
	docker-compose up
 
 upd:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

createsuperuser:
	docker-compose run app python3 manage.py createsuperuser

makemigrations:
	docker-compose run --rm app python3 manage.py makemigrations $(filter-out $@,$(MAKECMDGOALS))

migrate:
	docker-compose run --rm app python3 manage.py migrate $(filter-out $@,$(MAKECMDGOALS))

test:
	docker-compose run --service-ports  --rm app python3 manage.py test $(filter-out $@,$(MAKECMDGOALS))

lint:
	docker-compose run --rm app flake8