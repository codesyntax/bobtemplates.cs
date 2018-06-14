${buildout:directory}/var/log/*.log{
        daily
        rotate 7
        copytruncate
        compress
        notifempty
        missingok
        sharedscripts
        postrotate
          /bin/kill -USR2 `cat ${buildout:directory}/var/instance.pid`
          /bin/kill -USR2 `cat ${buildout:directory}/var/zeo.pid`
        endscript
}
