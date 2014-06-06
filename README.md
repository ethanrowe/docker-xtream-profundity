docker-xtream-profundity
========================

A deeply stupid docker image for playing with microservice architecture.

This is a really stupid application:

* You send it GET requests to any path
* It responds with application/json saying:
  * It's name
  * Your IP:port
  * The path you asked for
  * The current UTC time

You can run it without any arguments, and it will listen on port 8080 internally.

You can use environment variables to change the port it likes, or the name it uses in its responses.

* PROFOUND\_PORT controls the port
* PROFOUND\_NAME controls the name.

If you're going to have the app accessible from the host's IP then you need to launch the docker
container with the `-p` option to forward the relevant port.

