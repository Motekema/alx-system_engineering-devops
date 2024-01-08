# 2-puppet_custom_http_response_header.pp

class custom_http_response_header {
  package { 'nginx':
    ensure => present,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "# Custom Nginx configuration\nserver {\n\tlisten 80 default_server;\n\tserver_name _;\n\n\tlocation / {\n\t\tadd_header X-Served-By $hostname;\n\t\troot /var/www/html;\n\t\tindex index.html index.htm;\n\t}\n}\n",
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }
}

include custom_http_response_header

