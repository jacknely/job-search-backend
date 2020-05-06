To build image:
```
$ docker build -t job_search .
```

To run image in container:
```
$ docker run -v $(pwd):/opt -p 5001:5001 --rm job_search
```
Ensure commands are executed in app root directory