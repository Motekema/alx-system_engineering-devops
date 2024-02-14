# Puppet manifest to fix Apache 500 Internal Server Error

# Ensure Apache and PHP are installed
package { ['apache2', 'php5']:
  ensure => installed,
}

# Configure Apache to handle PHP files correctly
file { '/etc/apache2/mods-enabled/php5.load':
  ensure  => present,
  content => "LoadModule php5_module /usr/lib/apache2/modules/libphp5.so\n",
  require => Package['php5'],
}

# Restart Apache after configuration changes
service { 'apache2':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/apache2/mods-enabled/php5.load'],
}
