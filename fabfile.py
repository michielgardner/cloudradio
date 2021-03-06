from fabric.api import *
from config import config

env.hosts = [config['server_host']]
env.user = config['server_user']

def deploy():
  local("git archive --format=tar HEAD | gzip > deploy.tar.gz")
  run('rm -rf %s/code && mkdir -p %s/code' % (config['server_path'], config['server_path']))
  put('deploy.tar.gz', '%s/code/deploy.tar.gz' % config['server_path'])
  put('config.py', '%s/code/config.py' % config['server_path'])
  run("cd %s/code && tar zxf deploy.tar.gz && rm deploy.tar.gz" % config['server_path'])
  local('rm deploy.tar.gz')
  restart()

def restart():
  pass
