# -*- coding: utf-8 -*-

from base import generate_answers_ini

import glob
import subprocess


base_files = [
    '.editorconfig',
    'requirements.txt',
    'buildout.cfg',
    'deployment.cfg',
    'bobtemplate.cfg',
    'haproxy.cfg',
    'services.cfg',
    'varnish.cfg',
    'webserver.cfg',
    'templates/apache_complex.tpl',
    'templates/apache_ssl.tpl',
    'templates/apache.tpl',
    'templates/haproxy.tpl',
    'templates/logrotate.tpl',
    'templates/nginx_complex.tpl',
    'templates/nginx_ssl_http2.tpl',
    'templates/nginx_ssl.tpl',
    'templates/nginx.tpl',
]


def test_cs_plone_buildout(tmpdir, capsys, config):
    template = """[variables]
package.description = Dummy package
package.example = True
package.git.init = True
package.plone.version = 5.1.2
package.buildout_zope_port_number = 8080

author.name = CodeSyntax
author.email = info@codesyntax.com
author.github.user = codesyntax

plone.version = {version}
""".format(
        version=config.version
    )
    generate_answers_ini(tmpdir.strpath, template)

    config.template = 'cs_plone_buildout'
    config.package_name = 'project1'

    result = subprocess.call(
        [
            'mrbob',
            '-O',
            config.package_name,
            'bobtemplates.cs:' + config.template,
            '--config',
            'answers.ini',
            '--non-interactive',
        ],
        cwd=tmpdir.strpath,
    )
    assert result == 0

    generated_files = glob.glob(
        tmpdir.strpath + '/' + config.package_name + '/*'
    )
    length = len(tmpdir.strpath + '/' + config.package_name + '/')
    generated_files = [f[length:] for f in generated_files]
    required_files = base_files
    assert required_files <= generated_files
