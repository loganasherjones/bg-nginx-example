# Beer Garden with Nginx

In this example, I'm using nginx to proxy the Beer Garden API server.
The only ports that are exposed are 80 and all HTTP traffic goes
through nginx first.

## Setup

This requires:

- `git`
- `docker`
- `docker-compose`
- `python`

To get started simply:

```
git clone https://github.com/loganasherjones/bg-nginx-example
cd bg-nginx-example
docker-compose up -d
```

Then navigate to http://localhost/bg/

## Configuration

There are a couple of configurations you will need to modify to get
everything working on your own system. The main ones are the FQDNs
that are set in both `brew-view-config.yml` and `bartender-config.yml`.
If your FQDN is `foo.com` then you would change `logan.dev.com` to
`foo.com`.

The nginx configuration is setup to forward all HTTP traffic on port 80
to the Beer Garden API server listening on port 2337. Port 2337 is not
exposed to the host, but it could be if you wanted it to be, simply
modify the `docker-compose.yml`

## Remote plugins

There is an example of a remote-plugin in `remote-plugins/calc.py`.
This plugin connects to the API server through the nginx proxy.

This is simply to show that using nginx as a proxy service will work.
