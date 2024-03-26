ec2_instance { 'Puppet Agent':
    ensure              => present,
    name                => 'FromPuppet',
    region              => 'us-east-1',
    image_id            => 'ami-053b0d53c279acc90',
    instance_type       => 't2.small'
  }
