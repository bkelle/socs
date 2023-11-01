#
# PySNMP MIB module TCP-MIB (https://www.pysnmp.com/pysmi)
# ASN.1 source file://./TCP-MIB.mib
# Produced by pysmi-1.1.13 at Tue Oct 31 15:22:17 2023
# On host HAWKING platform Linux version 5.15.90.1-microsoft-standard-WSL2 by user davidvng
# Using Python version 3.8.8 (default, Apr 13 2021, 19:58:26) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, NotificationType, IpAddress, Bits, mib_2, ObjectIdentity, Unsigned32, Gauge32, Counter64, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "NotificationType", "IpAddress", "Bits", "mib-2", "ObjectIdentity", "Unsigned32", "Gauge32", "Counter64", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tcpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 49))
tcpMIB.setRevisions(('2005-02-18 00:00', '1994-11-01 00:00', '1991-03-31 00:00',))
if mibBuilder.loadTexts: tcpMIB.setLastUpdated('200502180000Z')
if mibBuilder.loadTexts: tcpMIB.setOrganization('IETF IPv6 MIB Revision Team http://www.ietf.org/html.charters/ipv6-charter.html')
tcp = MibIdentifier((1, 3, 6, 1, 2, 1, 6))
tcpRtoAlgorithm = MibScalar((1, 3, 6, 1, 2, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("constant", 2), ("rsre", 3), ("vanj", 4), ("rfc2988", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRtoAlgorithm.setStatus('current')
tcpRtoMin = MibScalar((1, 3, 6, 1, 2, 1, 6, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRtoMin.setStatus('current')
tcpRtoMax = MibScalar((1, 3, 6, 1, 2, 1, 6, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRtoMax.setStatus('current')
tcpMaxConn = MibScalar((1, 3, 6, 1, 2, 1, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpMaxConn.setStatus('current')
tcpActiveOpens = MibScalar((1, 3, 6, 1, 2, 1, 6, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpActiveOpens.setStatus('current')
tcpPassiveOpens = MibScalar((1, 3, 6, 1, 2, 1, 6, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpPassiveOpens.setStatus('current')
tcpAttemptFails = MibScalar((1, 3, 6, 1, 2, 1, 6, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpAttemptFails.setStatus('current')
tcpEstabResets = MibScalar((1, 3, 6, 1, 2, 1, 6, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpEstabResets.setStatus('current')
tcpCurrEstab = MibScalar((1, 3, 6, 1, 2, 1, 6, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpCurrEstab.setStatus('current')
tcpInSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpInSegs.setStatus('current')
tcpOutSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpOutSegs.setStatus('current')
tcpRetransSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRetransSegs.setStatus('current')
tcpInErrs = MibScalar((1, 3, 6, 1, 2, 1, 6, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpInErrs.setStatus('current')
tcpOutRsts = MibScalar((1, 3, 6, 1, 2, 1, 6, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpOutRsts.setStatus('current')
tcpHCInSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpHCInSegs.setStatus('current')
tcpHCOutSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpHCOutSegs.setStatus('current')
tcpConnectionTable = MibTable((1, 3, 6, 1, 2, 1, 6, 19), )
if mibBuilder.loadTexts: tcpConnectionTable.setStatus('current')
tcpConnectionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 19, 1), ).setIndexNames((0, "TCP-MIB", "tcpConnectionLocalAddressType"), (0, "TCP-MIB", "tcpConnectionLocalAddress"), (0, "TCP-MIB", "tcpConnectionLocalPort"), (0, "TCP-MIB", "tcpConnectionRemAddressType"), (0, "TCP-MIB", "tcpConnectionRemAddress"), (0, "TCP-MIB", "tcpConnectionRemPort"))
if mibBuilder.loadTexts: tcpConnectionEntry.setStatus('current')
tcpConnectionLocalAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 1), InetAddressType())
if mibBuilder.loadTexts: tcpConnectionLocalAddressType.setStatus('current')
tcpConnectionLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 2), InetAddress())
if mibBuilder.loadTexts: tcpConnectionLocalAddress.setStatus('current')
tcpConnectionLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 3), InetPortNumber())
if mibBuilder.loadTexts: tcpConnectionLocalPort.setStatus('current')
tcpConnectionRemAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 4), InetAddressType())
if mibBuilder.loadTexts: tcpConnectionRemAddressType.setStatus('current')
tcpConnectionRemAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 5), InetAddress())
if mibBuilder.loadTexts: tcpConnectionRemAddress.setStatus('current')
tcpConnectionRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 6), InetPortNumber())
if mibBuilder.loadTexts: tcpConnectionRemPort.setStatus('current')
tcpConnectionState = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcpConnectionState.setStatus('current')
tcpConnectionProcess = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnectionProcess.setStatus('current')
tcpListenerTable = MibTable((1, 3, 6, 1, 2, 1, 6, 20), )
if mibBuilder.loadTexts: tcpListenerTable.setStatus('current')
tcpListenerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 20, 1), ).setIndexNames((0, "TCP-MIB", "tcpListenerLocalAddressType"), (0, "TCP-MIB", "tcpListenerLocalAddress"), (0, "TCP-MIB", "tcpListenerLocalPort"))
if mibBuilder.loadTexts: tcpListenerEntry.setStatus('current')
tcpListenerLocalAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 20, 1, 1), InetAddressType())
if mibBuilder.loadTexts: tcpListenerLocalAddressType.setStatus('current')
tcpListenerLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 20, 1, 2), InetAddress())
if mibBuilder.loadTexts: tcpListenerLocalAddress.setStatus('current')
tcpListenerLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 20, 1, 3), InetPortNumber())
if mibBuilder.loadTexts: tcpListenerLocalPort.setStatus('current')
tcpListenerProcess = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 20, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpListenerProcess.setStatus('current')
tcpConnTable = MibTable((1, 3, 6, 1, 2, 1, 6, 13), )
if mibBuilder.loadTexts: tcpConnTable.setStatus('deprecated')
tcpConnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 13, 1), ).setIndexNames((0, "TCP-MIB", "tcpConnLocalAddress"), (0, "TCP-MIB", "tcpConnLocalPort"), (0, "TCP-MIB", "tcpConnRemAddress"), (0, "TCP-MIB", "tcpConnRemPort"))
if mibBuilder.loadTexts: tcpConnEntry.setStatus('deprecated')
tcpConnState = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcpConnState.setStatus('deprecated')
tcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnLocalAddress.setStatus('deprecated')
tcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnLocalPort.setStatus('deprecated')
tcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnRemAddress.setStatus('deprecated')
tcpConnRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnRemPort.setStatus('deprecated')
tcpMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 49, 2))
tcpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 49, 2, 1))
tcpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 49, 2, 2))
tcpMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 49, 2, 1, 2)).setObjects(("TCP-MIB", "tcpBaseGroup"), ("TCP-MIB", "tcpConnectionGroup"), ("TCP-MIB", "tcpListenerGroup"), ("TCP-MIB", "tcpHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpMIBCompliance2 = tcpMIBCompliance2.setStatus('current')
tcpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 49, 2, 1, 1)).setObjects(("TCP-MIB", "tcpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpMIBCompliance = tcpMIBCompliance.setStatus('deprecated')
tcpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 1)).setObjects(("TCP-MIB", "tcpRtoAlgorithm"), ("TCP-MIB", "tcpRtoMin"), ("TCP-MIB", "tcpRtoMax"), ("TCP-MIB", "tcpMaxConn"), ("TCP-MIB", "tcpActiveOpens"), ("TCP-MIB", "tcpPassiveOpens"), ("TCP-MIB", "tcpAttemptFails"), ("TCP-MIB", "tcpEstabResets"), ("TCP-MIB", "tcpCurrEstab"), ("TCP-MIB", "tcpInSegs"), ("TCP-MIB", "tcpOutSegs"), ("TCP-MIB", "tcpRetransSegs"), ("TCP-MIB", "tcpConnState"), ("TCP-MIB", "tcpConnLocalAddress"), ("TCP-MIB", "tcpConnLocalPort"), ("TCP-MIB", "tcpConnRemAddress"), ("TCP-MIB", "tcpConnRemPort"), ("TCP-MIB", "tcpInErrs"), ("TCP-MIB", "tcpOutRsts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpGroup = tcpGroup.setStatus('deprecated')
tcpBaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 2)).setObjects(("TCP-MIB", "tcpRtoAlgorithm"), ("TCP-MIB", "tcpRtoMin"), ("TCP-MIB", "tcpRtoMax"), ("TCP-MIB", "tcpMaxConn"), ("TCP-MIB", "tcpActiveOpens"), ("TCP-MIB", "tcpPassiveOpens"), ("TCP-MIB", "tcpAttemptFails"), ("TCP-MIB", "tcpEstabResets"), ("TCP-MIB", "tcpCurrEstab"), ("TCP-MIB", "tcpInSegs"), ("TCP-MIB", "tcpOutSegs"), ("TCP-MIB", "tcpRetransSegs"), ("TCP-MIB", "tcpInErrs"), ("TCP-MIB", "tcpOutRsts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpBaseGroup = tcpBaseGroup.setStatus('current')
tcpConnectionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 3)).setObjects(("TCP-MIB", "tcpConnectionState"), ("TCP-MIB", "tcpConnectionProcess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpConnectionGroup = tcpConnectionGroup.setStatus('current')
tcpListenerGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 4)).setObjects(("TCP-MIB", "tcpListenerProcess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpListenerGroup = tcpListenerGroup.setStatus('current')
tcpHCGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 5)).setObjects(("TCP-MIB", "tcpHCInSegs"), ("TCP-MIB", "tcpHCOutSegs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpHCGroup = tcpHCGroup.setStatus('current')
mibBuilder.exportSymbols("TCP-MIB", tcpActiveOpens=tcpActiveOpens, tcpConnRemAddress=tcpConnRemAddress, tcpListenerLocalAddressType=tcpListenerLocalAddressType, tcpMaxConn=tcpMaxConn, tcpCurrEstab=tcpCurrEstab, tcpListenerLocalPort=tcpListenerLocalPort, tcpConnLocalAddress=tcpConnLocalAddress, tcpListenerGroup=tcpListenerGroup, tcpConnectionRemPort=tcpConnectionRemPort, tcpRtoMin=tcpRtoMin, tcpListenerLocalAddress=tcpListenerLocalAddress, tcpConnState=tcpConnState, tcpHCOutSegs=tcpHCOutSegs, tcpInErrs=tcpInErrs, tcpConnectionEntry=tcpConnectionEntry, tcpRtoAlgorithm=tcpRtoAlgorithm, tcpOutRsts=tcpOutRsts, tcpRtoMax=tcpRtoMax, tcpListenerTable=tcpListenerTable, tcpConnectionRemAddress=tcpConnectionRemAddress, tcpGroup=tcpGroup, tcpMIBConformance=tcpMIBConformance, tcpListenerProcess=tcpListenerProcess, tcpConnEntry=tcpConnEntry, tcpOutSegs=tcpOutSegs, tcpMIB=tcpMIB, tcpPassiveOpens=tcpPassiveOpens, PYSNMP_MODULE_ID=tcpMIB, tcpHCGroup=tcpHCGroup, tcpBaseGroup=tcpBaseGroup, tcp=tcp, tcpConnectionProcess=tcpConnectionProcess, tcpRetransSegs=tcpRetransSegs, tcpConnTable=tcpConnTable, tcpConnectionState=tcpConnectionState, tcpMIBCompliances=tcpMIBCompliances, tcpMIBCompliance=tcpMIBCompliance, tcpConnectionLocalAddressType=tcpConnectionLocalAddressType, tcpAttemptFails=tcpAttemptFails, tcpMIBCompliance2=tcpMIBCompliance2, tcpConnectionTable=tcpConnectionTable, tcpHCInSegs=tcpHCInSegs, tcpEstabResets=tcpEstabResets, tcpInSegs=tcpInSegs, tcpConnectionGroup=tcpConnectionGroup, tcpConnRemPort=tcpConnRemPort, tcpMIBGroups=tcpMIBGroups, tcpConnLocalPort=tcpConnLocalPort, tcpConnectionLocalPort=tcpConnectionLocalPort, tcpListenerEntry=tcpListenerEntry, tcpConnectionLocalAddress=tcpConnectionLocalAddress, tcpConnectionRemAddressType=tcpConnectionRemAddressType)
