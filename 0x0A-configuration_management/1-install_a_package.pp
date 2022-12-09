# install flask 2.1.0

exec { 'flask':
  command => '/usr/bin/python install flask -v 2.1.0',
}
