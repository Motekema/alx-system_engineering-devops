# Puppet manifest to kill a process named "killmenow" using pkill

exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
}


