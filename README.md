# avamore-technical-test

## Backend

To install the dependencies for the Django backend, run the following command in terminal from the root directory.

```
make install-django
```

**Note:** The above script will install dependencies like Django to your local machine. If you'd prefer to use a virtual environment for the python requirements, please set up the environment and run the installations in the virtual environment. The backend directory in the Makefile will need to be changed to the virtual environment which hosts the backend. 

### Redemption Model

The logic for the redemption model is in redemptionModel.py under the model directory. The POST API endpoint is in views.py under the same directory.

## Frontend

To install the dependencies for the React frontend, run the following command in terminal from the root directory.

```
make install-react
```

**Note:** Please make sure you have Node.js installed in order to be able to use the npm command. You can check whether npm is installed using **npm -v** in terminal. 

### Redemption Model Interface

The HTML and frontend logic is in the redemptionInterface.js file under the src directory. The CSS styles applied to the HTML is in the styles.css file.


## Run Backend & Frontend

To run the backend server on port 8000 and the frontend server on port 3000, run the following command in the root directory:

```
make run
```

This will run the web interface on http://localhost:3000.

