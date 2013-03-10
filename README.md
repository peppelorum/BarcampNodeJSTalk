This is an example of how to use [Nginx's X-Accel-Redirect](http://www.wellfireinteractive.com/blog/nginx-django-x-accel-redirects/) to password protect static files, and at the same time use those files as CommonJS modules for a NodeJS server. These files are also added to the cache.manifest to show how to use them offline.

I was a bit lazy when doing this, so this is what you’ll end up with:

- A flask server (on port 8010)
- A nginx (on port 9010)
- A NodeJS server (on port 8020)

The requirements for the python part is flask and requests. The NodeJS needs CommonJS. And you need to use the nginx.conf but change the paths to match yours. I use foreman to start it all, so in Procfile you can see what commands that needs, or just run ‘foreman start’ and everything to be just fine and dandy.