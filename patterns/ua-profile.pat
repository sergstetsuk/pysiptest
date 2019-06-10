NOTIFY sip:6131@172.24.201.36 SIP/2.0
Via: SIP/2.0/UDP 172.24.201.36;rport;branch=branch-1
Max-Forwards: 70
To: <sip:6131@172.24.201.26>
From: <sip:6130@172.24.201.36>;tag=tag-1
Call-ID: test-notify
CSeq: 1 NOTIFY
Contact: <sip:6130@172.24.201.36>;expires=600
Max-Forwards: 67
Event: ua-profile
Subscription-State: active
P-Called-Party-ID: <sip:6131@172.24.201.36>
Content-Type: application/simservs+xml
Content-Length: AUTO

<?xml version="1.0"?>
<simservs>
<dial-tone-management>
<dial-tone-pattern>special-condition-tone</dial-tone-pattern>
</dial-tone-management>
</simservs>
