<VirtualHost *:80>
    ServerName ${configuration:server-name}

    RewriteEngine On

    RewriteCond %{HTTP_COOKIE} "__ac="
    RewriteRule ^(.*) http://${configuration:edit-server-name}:80$1 [L]
    RewriteRule (.*)(/login|/require_login|/failsafe_login_form)(.*) http://${configuration:edit-server-name}:80$1$2$3 [R]

    # Zope directly
    RewriteRule ^/(.*) http://127.0.0.1:${ports:instance}/VirtualHostBase/http/%{HTTP_HOST}:80/Plone/VirtualHostRoot/$1 [L,P]
    # Varnish
    # RewriteRule ^/(.*) http://127.0.0.1:${ports:varnish}/VirtualHostBase/http/%{HTTP_HOST}:80/Plone/VirtualHostRoot/$1 [L,P]
    # HAProxy
    # RewriteRule ^/(.*) http://127.0.0.1:${ports:haproxy}/VirtualHostBase/http/%{HTTP_HOST}:80/Plone/VirtualHostRoot/$1 [L,P]

    ErrorLog ${configuration:apache-log-path}/${configuration:server-name}.error.log
    CustomLog ${configuration:apache-log-path}/${configuration:server-name}.access.log combined

    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/json
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/x-javascript
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/xml+rss
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/javascript
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/xml

</VirtualHost>

<VirtualHost *:80>
    ServerName ${configuration:edit-server-name}

    RewriteEngine On

    RewriteCond %{HTTP_COOKIE} "__ac=" [OR]
    RewriteCond %{REQUEST_URI} ^.*(/login|/login_form|/require_login|/failsafe_login_form|logged_out)$

    RewriteRule ^/(.*) http://127.0.0.1:${configuration:zope-edit-port}/VirtualHostBase/http/%{HTTP_HOST}:80/Plone/VirtualHostRoot/$1 [L,P]

    RewriteRule ^/(.*) http://${configuration:server-name}/$1 [C]

    ErrorLog ${configuration:apache-log-path}/${configuration:edit-server-name}.error.log
    CustomLog ${configuration:apache-log-path}/${configuration:edit-server-name}.access.log combined

    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/json
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/x-javascript
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/xml+rss
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/javascript
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/xml

</VirtualHost>

<VirtualHost *:80>
  ServerName ${configuration:server-name-principal-redirect}
  ServerAlias ${configuration:additional-names}
  RewriteEngine On

  RewriteRule ^/(.*) http://${configuration:server-name}/$1 [L,R=301]

</VirtualHost>
