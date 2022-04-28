# Running Project Redis
` This project is for showing you the use of Redis `<br>
` Redis is an in-memory data structure store that can be used as a caching engine. Since it keeps data in RAM, Redis can deliver it very quickly.`

<hr>

### installing redis :
1. goto https://redis.io/docs/getting-started/ <br>
2. Install redis according your OS platform <br>
3. if your os is mac & you aren't able to install redis using brew then follow below: <br>
    1. on command line, type 'mkdir redis && cd redis <br>
    2. then type 'curl -O http://download.redis.io/redis-stable.tar.gz'
    3. then type 'tar xzvf redis-stable.tar.gz'
    4. then type 'cd redis-stable'
    5. then type 'make'
    6. then type 'make test'
    7. then type 'sudo make install'
    8. sudo cp redis/src/redis-cli /usr/local/bin/ && sudo cp redis/src/redis-server /user/local/bin/
    9. test your redis by running 'redis-server' & in new terminal 'redis-cli ping' if it return pong then it should be working & if not then someproblem is there. You can stop redis-server by pressing ctrl + c.

<hr>

## If you want to setup quickly have the project running up

1. git clone git@github.com:feignbird/project_redis.git <br>
` Clone the project `

2. cd project_redis <br>
` Change dir `

3. chmod 744 run.sh <br>
` Change permission of run.sh `

4. ./run.sh <br>
` execute run.sh ` <br>
` while running any pop-up comes then press 'OK' `<br>
` Create super user`

` Note:`<br>
` if your port is already in use then run` <br>
source redis-env/bin/activate<br>
python manage.py runserver 0.0.0.0:8081 `<- [input_port_that_is_not_in_use] `<br>

<hr>

## Follow below shown commands to run the program by writing each command yourself

run redis-server on a terminal
run redis-cli on another terminal


1. python3 -m venv redis-env <br>
` Above command will setup a python virtual environment named as 'redis-env', A virtual environment is needed beacause its good to source all our installed dependencies from a local environment & also, it helps running multiple projects on the same computer at the same time, with their own virtual environment.`

2. source redis-env/bin/activate <br>
` Above command will tell terminal/computer that for this project source all the dependencies from 'redis-env' VE`

3. python3 -m pip install --upgrade pip <br>
` Above command will upgrade the pip package on our VE `

4. pip install -r requirements.txt <br>
` Above command will install the dependecies mentioned in requirements.txt file.`

5. cd api <br>
` Above command will change the directory you are working on to 'api' named dir `

6. python manage.py makemigrations && python manage.py migrate <br>
` Above command will migrate the migrations `

7. python manage.py createsuperuser <br>
` By using Above command you can create a superuser for logging in the ADMIN panel `


` By using below shown commands, you can use python shell of the VE & execute necessary functions `
8. python manage.py shell <br>
    1. from redis_app.data_create import create_tables
    2. create_tables()
    <pre> 
    Wait till finished
    </pre>
    3. exit()


9. python manage.py runserver 0.0.0.0:9000 <br>
` Above will run your django project `




`Now you can hit 'http://0.0.0.0:9000/get-a/' url to get the data of 'table A' & it can take a minute, Now next time you hit the url again redis will show its magic.....the response will be fast (in ms), If you want to clear the redis simply hit 'http://0.0.0.0:9000/clear-cache/' url & the redis DB will be flushed`



## API Endpoints
### There are total of 7 endpoints <br>
` First time -> you hit the GET request at any endpoint -> it will take some time & the response is also cached in redis for 2 minutes` <br>
` Next time -> you hit the GET request at any endpoint -> it will be fast because the cached data is coming ` <br>
1. GET http://localhost:9000/get-e/ <- Gives data of table E 
2. GET http://localhost:9000/get-d/ <- Gives data of table D
3. GET http://localhost:9000/get-c/ <- Gives data of table C
4. GET http://localhost:9000/get-b/ <- Gives data of table B
5. GET http://localhost:9000/get-a/ <- Gives data of table A
6. GET http://localhost:9000/clear-cache/ <- It'll clear the cache in redis
7. Goto URL: http://localhost:9000/admin/ <- Log into admin panel
8. GET http://localhost:9000/swagger.json <- get swagger.json data
9. Goto URL: http://localhost:9000/swagger/ <- Opens up swagger for the project
10. Goto URL: http://localhost:9000/redoc/ <- Opens up redoc generator for project <br>

<h3> First of all redis should be installed correctly </h3>
<h3> refer above if you haven't </h3>

### How to work with redis
1. pip install django-redis && pip install redis
2. add cache configuration settngs like shown below
     <pre> 
     CACHE = {
        'default':{
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': 'redis://localhost:6379',
            'TIMEOUT': 600, # in seconds
            'KEY_PREFIX': "some_name"
        }
    }
    CACHE_TTL = 60 * 2 # (in seconds)
    </pre>

3. apply cache on view functions 
    <pre>
    from django.utils.decorators import method_decorator
    from django.views.decorators.cache import cache_page
    from django.views.decorators.vary import vary_on_cookie
    from django.conf import settings
    CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

    # views.py
    class SomeViewSet(viewsets.ModelViewset):
        queryset = Something
        serializer_class = SomethingSerializer
        ...
        @method_decorator(vary_on_cookie)
        @method_decorator(cache_page(CACHE_TTL))
        def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)
    </pre>

4. if you want to do some other things you can refer to below links
    1. https://docs.djangoproject.com/en/4.0/topics/cache/
    2. https://realpython.com/caching-in-django-with-redis/
    3. https://django-redis-cache.readthedocs.io/en/latest/
    4. https://tute.io/how-to-cache-django-rest-framework-with-redis
    5. https://redis.io/docs/manual/data-types/data-types-tutorial/
