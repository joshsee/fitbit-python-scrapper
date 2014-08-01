notify { 'Preparing box': }

exec { "apt-get update":
  command => "/usr/bin/apt-get update",
  before => Exec["apt-get install python-pip"],
  logoutput => on_failure
}

exec { "apt-get install python-pip":
  command => "/usr/bin/apt-get install python-pip -y"
}

exec { "apt-get install python-dev libxml2-dev libxslt-dev make gcc":
  command => "/usr/bin/apt-get install python-dev libxml2-dev libxslt-dev make gcc -y"
}

