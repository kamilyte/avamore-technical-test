install-django:
	pip install -r requirements-django.txt

install-react:
	bash -c "cd part-2/frontend/part2 && npm install"

django:
	bash -c "python part-2/backend/part2/manage.py runserver"

react:
	bash -c "cd part-2/frontend/part2 && npm start"

run:
	make django & make react 

