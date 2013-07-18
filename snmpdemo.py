from pysnmp import debug
from pysnmp.entity.rfc3413.oneliner import ntforg

debug.setLogger(debug.Debug('all'))

ntfOrg = ntforg.NotificationOriginator()

errorIndication = ntfOrg.sendNotification(
    ntforg.CommunityData('$mtSNMPr%'),
    ntforg.UdpTransportTarget(('10.200.23.6 ', 162)),
    'trap',
    ntforg.MibVariable('SNMPv2-MIB', 'coldStart'),
    (ntforg.MibVariable('SNMPv2-MIB', 'sysName', 0), 'new name')
)

if errorIndication:
    print('Notification not sent: %s' % errorIndication)