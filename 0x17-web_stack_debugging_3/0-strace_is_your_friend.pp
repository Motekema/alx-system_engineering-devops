# Puppet manifest to fix Apache 500 Internal Server Error

# Ensure Apache and PHP are installed
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
