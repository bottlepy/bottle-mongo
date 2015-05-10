config = {
  _id: 'testReplSet',
  members: [
    {_id: 0, host: 'travis:27017'},
    {_id: 2, host: 'travis:27018'},
  ]
}

printjson(rs.initiate(config));
printjson(rs.status());

// Little bit of javascript that waits for the replicaSet to become ready
var attempts = 50;
while (--attempts > 0) {

  var rs_status = rs.status();;
  printjson(rs_status);

  if (rs_status.ok) {

    if (rs_status.members.length >= 2) {

      var has_primary = rs_status.members.some(function(m) {
         return (m.state == 1);
      });

      var has_secondary = rs_status.members.some(function(m) {
        return (m.state == 2);
      });

      if (has_primary && has_secondary) {
        break;
      }

    }

  }

  sleep(2000);
}

if (attempts == 0) {
  quit(1);
}

// vim: sts=2 sw=2 ts=2 et
