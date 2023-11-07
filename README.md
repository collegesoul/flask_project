## A Simple Flask API 

This is a flask api that accepts GET, POST and PUT
HTTP requests. It connects to a mongodb database to
create, read and update key-value objects.

<br>

### API Endpoints

| Method   | URL Pattern           | Description                                               |
|----------|-----------------------|-----------------------------------------------------------|
| **GET**  | `"/api/v1/keys"`      | Gets all key-value objects                                |
| **GET**  | `"/api/v1/key/<key>"` | Gets only one key-value object matching the requested key |
| **POST** | `"/api/v1/key"`       | Creates new key-value object                              |
| **PUT**  | `"/api/v1/key"`       | Updates a key-value object matching the requested key     |

<br>

### *Body Payload for POST and PUT Request*

The Body parameters should be written in this way to avoid errors:<br>
```
{
    "key": "key of type string",
    "value": "value of any type"
}
```

**NOTE:** The keys are unique and do not accept duplicates. It returns a *'key already exists'* error
if you try to create a key that already exists.

<br>

### *DockerFile and Docker-Compose.yml*
There's a Dockerfile to dockerize the flask app. A docker-compose.yml is provided for linking the 
flask app to the mongodb database. The flask app uses the port `8080` and the monogodb uses its standard
port `27017`.<br><br>
To run the docker-compose.yml file use:<br>
`docker-compose up` or `sudo docker-compose up`<br>
*Make sure docker compose is installed to run the docker-compose command*

<br>

### *Environment Variables*
These environment variables need to be set for the flask app to work well. The variables can be stored 
in an .env file. For using environment variables without the .env file the `docker-compose.yml` can be edited
to read those variables.<br><br>
**In the .env file:**<br>
```
#Mongodb User Information for Flask
MONGODB_USERNAME=<mongo_username>
MONGODB_PASSWORD=<mongo_password>
MONGODB_HOSTNAME=mongodb

#Mongodb Authentication
MONGO_INITDB_ROOT_USERNAME=<mongo_username>
MONGO_INITDB_ROOT_PASSWORD=<mongo_password>
```