## About this project
In this project I use selenium to render pages in bind with Redis and Dramatiq for performing 
asynchronous tasks (in this case - rendering pages).
## How does it work?
Firstly, you need to send the request with url and headers.
After this, you will get a unique link where the response will be available after rendering.
Thanks to async queue, the page rendering will occur depending on the server performance, which 
helps to avoid problems with HTTP timeout and hanging server on a large number of requests.
With a heavy load on the server, you can refer to your link later and get your response. 
You don't need to wait long time for response, just store links and take it a litle bit later.
## How to run project?

1. Clone repository to your server
2. Download chromedriver from https://chromedriver.chromium.org/downloads and extract it in your project directory (i am using 103 version) 
3. `docker-compose build`
4. `docker-compose up`
5. This is an exmaple link: http://0.0.0.0/get_page/?url=http://google.com, you can test it.