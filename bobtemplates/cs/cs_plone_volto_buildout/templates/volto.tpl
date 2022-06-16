# Reference SSL: https://mozilla.github.io/server-side-tls/ssl-config-generator/

upstream ${buildout:projectname}volto {
    server 127.0.0.1:3000;
}

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
    ssl_session_timeout 1d;
    ssl_session_cache shared:MozSSL:10m;  # about 40000 sessions
    ssl_session_tickets off;

    # Diffie-Hellman parameter for DHE ciphersuites, recommended 2048 bits
    # Generate this file running as root the following command:
    #  $ mkdir -p /etc/nginx/ssl
    #  $ openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048
    ssl_dhparam /etc/nginx/ssl/dhparam.pem;

    # intermediate configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;

    # HSTS (ngx_http_headers_module is required) (63072000 seconds)
    add_header Strict-Transport-Security "max-age=63072000" always;

    # OCSP stapling
    ssl_stapling on;
    ssl_stapling_verify on;

    resolver 8.8.8.8;

    # Content-Security-Policy
    #add_header Content-Security-Policy "default-src 'self' https://* data: ; img-src https://* data: 'self' 'unsafe-inline'; child-src 'none'; base-uri 'self'; form

    # Permissions-Policy
    add_header Permissions-Policy "accelerometer=(), ambient-light-sensor=(), autoplay=(), camera=(), encrypted-media=(), fullscreen=(self), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), midi=(), payment=(), picture-in-picture=(), sync-xhr=(self), usb=(), speaker=(), vr=()";

    # Referrer-Policy
    add_header Referrer-Policy same-origin;

    # Extra Headers
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options SAMEORIGIN always;

    # Block pages from loading when they detect reflected XSS attacks
    add_header X-XSS-Protection "1; mode=block";

    server_name ${configuration:server-name} ;
    access_log ${configuration:nginx-log-path}/${configuration:server-name}.log;
    error_log  ${configuration:nginx-log-path}/${configuration:server-name}.error.log;

    gzip            on;
    gzip_min_length 1000;
    gzip_types      application/javascript application/json application/rss+xml application/x-javascript application/xhtml+xml application/xml application/xml+rss text/css text/html text/javascript text/plain text/xml;

    client_max_body_size 20M;

    location ~ /api($|/.*) {
        rewrite ^/api($|/.*) /VirtualHostBase/https/${configuration:server-name}:443/Plone/VirtualHostRoot/_vh_api$1 break;
        proxy_pass http://${buildout:projectname}plone;
        # Varnish
        # proxy_pass http://${buildout:projectname}varnish;
        # HAProxy
        # proxy_pass http://${buildout:projectname}haproxy;
    }

    location ~ /\+\+api\+\+($|/.*) {
        rewrite ^/\+\+api\+\+($|/.*) /VirtualHostBase/https/${configuration:server-name}:443/Plone/++api++/VirtualHostRoot/$1 break;
        proxy_pass http://${buildout:projectname}plone;
        # Varnish
        # proxy_pass http://${buildout:projectname}varnish;
        # HAProxy
        # proxy_pass http://${buildout:projectname}haproxy;
    }

    location ~ / {
        location ~* \.(js|jsx|css|less|swf|eot|ttf|otf|woff|woff2)$ {
            add_header Cache-Control "public";
            expires +1y;
            proxy_pass http://${buildout:projectname}volto;
        }
        location ~* static.*\.(ico|jpg|jpeg|png|gif|svg)$ {
            add_header Cache-Control "public";
            expires +1y;
            proxy_pass http://${buildout:projectname}volto;
        }

        proxy_set_header        Host $host;
        proxy_set_header        X-Real-IP $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header        X-Forwarded-Proto $scheme;
        proxy_redirect http:// https://;
        proxy_pass http://${buildout:projectname}volto;
    }

}

server {

   listen 80;
   server_name ${configuration:server-name} ${configuration:additional-names};
   return 301 https://${configuration:server-name}$request_uri;
}
