from fabric.api import *
from config import config

env.hosts = [config['server_host']]
env.user = config['server_user']

def deploy():
  local("git archive --format=tar HEAD | gzip > deploy.tar.gz")
  run('rm -rf %s && mkdir -p %s' % (config['server_path'], config['server_path']))
  put('deploy.tar.gz', '%s/deploy.tar.gz' % config['server_path'])
  run("cd %s && tar zxf deploy.tar.gz && rm deploy.tar.gz" % config['server_path'])
  local('rm deploy.tar.gz')
  restart()

def restart():
  pass
