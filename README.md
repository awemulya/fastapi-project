# backend template

Template is meant to be a model how projects is build in fastapi.

## Build image

Use docker build command to build  project

```bash
cd fastapi-project
sudo docker-compose up -d --build
```

## Test

```
sudo docker-compose exec web pytest
```


## Check project running 

```
http://localhost:8002
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

