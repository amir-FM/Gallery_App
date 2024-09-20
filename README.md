# Gallery_App

Multiuser **Docker + Flask + Jinja2 + MongoDB** photo-managing web app.

![demo](https://github.com/user-attachments/assets/299b098c-9130-4986-b1a7-472c8e5e207f)

## Description

The application is split up into docker containers and run via a docker-compose file. The **flask** container is built using a *Dockerfile*, on an *Alpine Linux* image and used for the web app and picture storage. The user database is on an *MongoDB* container.

**Note:** The photo storage **is not** persistent and will reset at every rebuild of the **flask** container.

## How to Run

``` sh
git clone https://github.com/amir-FM/Gallery_App [installation directory]
cd [installation directory]
docker-compose up --build
```
