exec { 'apt-update':
  command => 'apt-get -y update',
  path    => ['/usr/bin', '/bin'],
  before  => Class['nginx'],
}

package { 'nginx':
  ensure => installed,
  before => File['/etc/nginx/sites-available/default'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

exec { 'ufw-allow-http':
  command => 'ufw allow \'Nginx HTTP\'',
  path    => ['/usr/bin', '/bin'],
  require => Package['nginx'],
}

file { '/data/web_static/':
  ensure => directory,
}

file { '/data/web_static/releases/test/':
  ensure => directory,
}

file { '/data/web_static/shared/':
  ensure => directory,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

exec { 'chown-ubuntu':
  command => 'chown -R ubuntu:ubuntu /data',
  path    => ['/usr/bin', '/bin'],
}

file_line { 'nginx-location':
  path    => '/etc/nginx/sites-available/default',
  line    => 'location /hbnb_static/ { alias /data/web_static/current/; }',
  match   => 'listen 80 default_server',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

exec { 'nginx-restart':
  command     => 'service nginx restart',
  path        => ['/usr/bin', '/bin'],
  refreshonly => true,
  subscribe   => File_line['nginx-location'],
}

exec { 'exit':
  command => 'exit 0',
  path    => ['/usr/bin', '/bin'],
  returns => [0],
}
