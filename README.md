# Webargs and aiohttp

#### A Prettier, simpler and straight forward code example of handling request arguments in aiohttp
requires `python3` for code and `curl` for examples.
This demo uses the [webargs library](https://webargs.readthedocs.io/en/latest/index.html) 
#### Installation 
```
pip3 install -r requirements.txt
```

#### Run 
```
python3 aiohttp-webargs-demo.py
```

##Examples of request

|Request|Response|
|-------|--------|
|`curl -X GET http://localhost:8080/hello `| Hello, World|
|`curl -X GET 'http://localhost:8080/hello?name=دنیا'`| Hello, دنیا|
|`curl -X GET 'http://localhost:8080/coro_hello?name=دنیا'`| Hello, دنیا|
|`curl -X GET 'http://localhost:8080/async_hello?name=دنیا'`| Hello, دنیا|

#### Missing values
Request

`curl -X GET http://localhost:8080/coro_age`

Response
```
{
    "age": [
        "Missing data for required field."
    ]
}
```  
#### Default Values
Request

`curl -X GET localhost:8080/coro_age?age=21`

Response

`You're age * number is 21`

#### Dirty Values
Request

`curl -X GET localhost:8080/coro_age?age=TwentyOne`

Response

```
{
    "age": [
        "Not a valid integer."
    ]
}
```
### Demo

<a href="https://asciinema.org/a/20lu8YOSrQLzPcpSp1vCzCsQZ" target="_blank"><img src="https://asciinema.org/a/20lu8YOSrQLzPcpSp1vCzCsQZ.svg" /></a>
