## URL Shortener Python Challenge

The challenge is to create an API to shorten urls, in the style that TinyURL and bit.ly made popular.

## Rules

1. The service must expose HTTP endpoints according to the definition below.
2. The service must be self contained, built on Python using Flask and able to be installed locally by following the steps you write in the README.
3. Write acceptance tests for your endpoints.
5. A data store is not required but it is a nice to have.


-------------------------------------------------------------------------

## Setup

run
```
docker-compose build
```
to build the project.

Then

```docker-compose up```

System will be running on localhost:8000.

First Add some data with POST to the system and then try to navigate via short code.


## API Documentation

**All responses must be encoded in JSON and have the appropriate Content-Type header**


### POST api/shorten

```
POST api/shorten
Content-Type: "application/json"

{
  "url": "http://example.com",
  "shortcode": "example"
}
```

Attribute | Description
--------- | -----------
**url**   | url to shorten
shortcode | preferential shortcode

##### Returns:

```
201 Created
Content-Type: "application/json"

{
  "shortcode": :shortcode
}
```

A random shortcode is generated if none is requested, the generated short code has exactly 6 alpahnumeric characters and passes the following regexp: ```^[0-9a-zA-Z_]{6}$```.

##### Errors:

Error | Description
----- | ------------
400   | ```url``` is not present
409   | The the desired shortcode is already in use. **Shortcodes are case-sensitive**.
422   | The shortcode fails to meet the following regexp: ```^[0-9a-zA-Z_]{4,}$```.


### GET api/:shortcode

```
GET api/:shortcode
Content-Type: "application/json"
```

Attribute      | Description
-------------- | -----------
**shortcode**  | url encoded shortcode

##### Returns

**302** response with the location header pointing to the shortened URL

```
HTTP/1.1 302 Found
Location: http://www.example.com
```

##### Errors

Error | Description
----- | ------------
404   | The ```shortcode``` cannot be found in the system

### GET api/:shortcode/stats

```
GET api/:shortcode/stats
Content-Type: "application/json"
```

Attribute      | Description
-------------- | -----------
**shortcode**  | url encoded shortcode

##### Returns

```
200 OK
Content-Type: "application/json"

{
  "start_date": "2012-04-23T18:25:43.511Z",
  "last_seen_date": "2012-04-23T18:25:43.511Z",
  "redirect_count": 1
}
```

Attribute          | Description
------------------ | -----------
**start_date**     | date when the url was encoded, conformant to [ISO8601](http://en.wikipedia.org/wiki/ISO_8601)
**redirect_count** | number of times the endpoint ```GET /shortcode``` was called
last_seen_date     | date of the last time the a redirect was issued, not present if ```redirectCount == 0```

##### Errors

Error | Description
----- | ------------
404   | The ```shortcode``` cannot be found in the system





