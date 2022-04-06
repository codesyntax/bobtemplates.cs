# Reference: http://www.starzel.de/blog/securing-plone-sites-with-https-and-nginx

upstream ${buildout:projectname}plone {
    server 127.0.0.1:${ports:instance};
}

upstream ${buildout:projectname}varnish {
    server 127.0.0.1:${ports:varnish};
}

upstream ${buildout:projectname}haproxy {
    server 127.0.0.1:${ports:haproxy};
}

server {

    listen 80;
    server_name ${configuration:server-name};
    access_log ${configuration:nginx-log-path}/${configuration:server-name}.log;
    error_log  ${configuration:nginx-log-path}/${configuration:server-name}.error.log;

    gzip            on;
    gzip_min_length 1000;
    gzip_types      application/javascript application/json application/rss+xml application/x-javascript application/xhtml+xml application/xml application/xml+rss text/css text/html text/javascript text/plain text/xml;

    client_max_body_size 20M;

    location / {
        rewrite ^/(.*)$ /VirtualHostBase/http/${configuration:server-name}:80/Plone/VirtualHostRoot/$1 break;
        # Directly Zope
        proxy_pass http://${buildout:projectname}plone;
        # Varnish
        # proxy_pass http://${buildout:projectname}varnish;
        # HAProxy
        # proxy_pass http://${buildout:projectname}haproxy;
    }
}


server {

   listen 80;
   server_name ${configuration:additional-names};
   return 301 $scheme://${configuration:server-name}$request_uri;
}
