# Realtime Data Logging and Visualization App Backend

The Realtime Data Logging and Visualization App Backend is the server-side component of the web application. It provides the API endpoints and handles the data processing and communication with the frontend.

## Installation

1.  Make sure you have Python and pipenv installed on your system.

2.  Clone the repository:

    ```shell
    git clone <repository_url>

    ```

3.  Navigate to the backend directory:

    ```shell
    cd backend
    ```

4.  Install the dependencies using pipenv:

    ```shell
    pipenv install
    ```

    Note: Ensure that you have pipenv installed. If not, you can install it using pip:

        pip install pipenv

5.  Activate the virtual environment:

    ```shell
    pipenv shell
    ```

6.  Apply the migrations:

    ```shell
    python manage.py migrate
    ```

7.  (Optional) Load sample data (if available):

    ```shell
    python manage.py loaddata <fixture_file>
    ```

8.  To start the backend server, run the following command:

    ```shell
    python manage.py runserver
    ```

# Dependencies

The following packages are used in the backend:

-   django = "\*"
-   django-cors-headers = "\*"
-   djangorestframework = "\*"
-   channels = {extras = ["daphne"], version = "\*"}
-   channels-redis = "\*"
-   django-jazzmin = "\*"
-   djoser = "\*"
