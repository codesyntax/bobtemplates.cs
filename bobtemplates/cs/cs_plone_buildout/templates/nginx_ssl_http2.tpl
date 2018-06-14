# Reference SSL: https://mozilla.github.io/server-side-tls/ssl-config-generator/

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
    listen 443 ssl http2;

    # certs sent to the client in SERVER HELLO are concatenated in ssl_certificate
    ssl_certificate ${configuration:ssl-certificate-path};
    ssl_certificate_key ${configuration:ssl-private-key-path};
    ssl_session_timeout 5m;
    ssl_session_cache shared:SSL:50m;

    # Diffie-Hellman parameter for DHE ciphersuites, recommended 2048 bits
    # Generate this file running as root the following command:
    #  $ mkdir -p /etc/nginx/ssl
    #  $ openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048
    ssl_dhparam /etc/nginx/ssl/dhparam.pem;

    # modern configuration. tweak to your needs.
    ssl_protocols TLSv1.2 TLSv1.1 TLSv1;
    ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK';
    ssl_prefer_server_ciphers on;

    # HSTS (ngx_http_headers_module is required) (15768000 seconds = 6 months)
    add_header Strict-Transport-Security max-age=15768000;

    resolver 8.8.8.8;

    server_name ${configuration:server-name} ;
    access_log ${configuration:nginx-log-path}/${configuration:server-name}.log;
    error_log  ${configuration:nginx-log-path}/${configuration:server-name}.error.log;

    gzip            on;
    gzip_min_length 1000;
    gzip_types      application/javascript application/json application/rss+xml application/x-javascript application/xhtml+xml application/xml application/xml+rss text/css text/html text/javascript text/plain text/xml;

    client_max_body_size 20M;

    location / {
        rewrite ^/(.*)$ /VirtualHostBase/https/${configuration:server-name}:443/Plone/VirtualHostRoot/$1 break;
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
   server_name ${configuration:server-name} ${configuration:additional-names};
   return 301 https://${configuration:server-name}$request_uri;
}
