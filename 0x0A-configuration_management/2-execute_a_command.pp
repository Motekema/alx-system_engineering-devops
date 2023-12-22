# Puppet manifest to kill a process named "killmenow" using pkil

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
