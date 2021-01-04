# Service for handling of devices in a Motorola radio system.

## Usage

### Storage of radio profiles
This is done using:
`POST /radios/{id}`
with a payload of the form

```json
{
“alias”: string,
“allowed_locations”: array<string>
}
```
The json response is None.
The standard response is "200 OK"

### Setting a location
This is done using:
`POST /radios/{id}/location `
with a payload of the form

```json
{
“location”: string
}
```
The json response is None.
The standard response is "200 OK" for valid location
The standard response is "403 FORBIDDEN" for invalid location
### Retrieval of radio's location

This is done using:
`GET /radios/{id}/location`

The json response is None if no location exists.
The standard response is "404 NOT FOUND" if no location exists.

The json response if the location exists:
```json
{
“location”: string
}
```
The standard response is "200 OK" for existing location

### Data Storage
The information is stored in python dictonaries. So, all information is lost when the server stops running.
