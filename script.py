import click
from subprocess import call

class Template:
    def __init__(self, name, content):
        self.name = name
        self.content = content

def bashTemplate():
    return Template('bash', '#!/usr/bin/env bash\n\n\n')
def zshTemplate():
    return Template('zsh', '#!/usr/bin/env zsh\n\n\n')
def shTemplate():
    return Template('sh', '#!/usr/bin/env sh\n\n\n')
def jshellTemplate():
    return Template('jshell', '//usr/bin/env jshell "$0" "$@"; exit $?\n\n\n\n/exit')
def jsTemplate():
    return Template('js', '#!/usr/bin/env node\n\n\n')
def nodeTemplate():
    return Template('node', '#!/usr/bin/env node\n\n\n')
    
templates = [
    bashTemplate(),
    zshTemplate(),
    shTemplate(),
    jshellTemplate(),
    jsTemplate(),
    nodeTemplate()
]

def getTemplate(name):
    if name:
        for template in templates:
            if template.name == name:
                return template.content
    return None
    
@click.command()
@click.option('--template', help='Template name for the new file.', required=True)
@click.argument('file', type=click.File('w'))
def cli(file, template):
    """Creates script file from templates"""
    content = getTemplate(template)
    if content:
        file.write(content)
