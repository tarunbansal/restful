# restful
Rest API sample using Python and Flask

1> To get list of all states :
URI : http://localhost:5000/states/api/v1.0/getstates

```
Sample request : "curl -i http://localhost:5000/states/api/v1.0/getstates"

Response: 

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 3441
Server: Werkzeug/0.9.6 Python/3.3.1
Date: Sun, 28 Feb 2016 15:56:32 GMT

{
  "states": [
    {
      "abbreviation": "AL", 
      "name": "Alabama"
    }, 
    {
      "abbreviation": "AK", 
      "name": "Alaska"
    },
    ..
    {
      "abbreviation": "WI", 
      "name": "Wisconsin"
    }, 
    {
      "abbreviation": "WY", 
      "name": "Wyoming"
    }
  ]
}
```

> Total 50 states data returned.

2> To get paginated results from the API

URI : http://localhost:5000/states/api/v1.0/getstates/[begIndex]?size=[int_Size]

Replace : begIndex with the value of next_val returned in previous request's headers.
	  int_size with the value of results to be displayed on each page.

```
Sample request: "curl -i http://localhost:5000/states/api/v1.0/getstates/0?size=10"

Response :

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 698
Next-Val: 10
Server: Werkzeug/0.9.6 Python/3.3.1
Date: Sun, 28 Feb 2016 16:05:04 GMT

{
  "states": [
    {
      "abbreviation": "AL", 
      "name": "Alabama"
    }, 
    {
      "abbreviation": "AK", 
      "name": "Alaska"
    }, 
    {
      "abbreviation": "AZ", 
      "name": "Arizona"
    }, 
    {
      "abbreviation": "AR", 
      "name": "Arkansas"
    }, 
    {
      "abbreviation": "CA", 
      "name": "California"
    }, 
    {
      "abbreviation": "CO", 
      "name": "Colorado"
    }, 
    {
      "abbreviation": "CT", 
      "name": "Connecticut"
    }, 
    {
      "abbreviation": "DE", 
      "name": "Delaware"
    }, 
    {
      "abbreviation": "FL", 
      "name": "Florida"
    }, 
    {
      "abbreviation": "GA", 
      "name": "Georgia"
    }
  ]
}
```

> Total 10 states data returned.
> "Next-Val: 10" returned in response header indicates the client to set [begIndex] as 10 in next request.
> "Next-Val" be returned as "-1" if no more records are left to be displayed.

3> Resource not found request

```
Sample request: "curl -i http://localhost:5000/states/api/v1.0/getstates/abc"

Response :

HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 30
Server: Werkzeug/0.9.6 Python/3.3.1
Date: Sun, 28 Feb 2016 17:12:40 GMT

{
  "errorCode": "Not found"
}
```

> No states returned.
> "errorCode":"Not found" is returned whenever resource is not found.
