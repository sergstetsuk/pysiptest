# pysiptest
Python based SIP testing tool
This project is inspired by [[https://github.com/SIPp/sipp]]. Although sipp is
a great tool I found some difficulties during creating custom scenarios with
fully customized SIP messages. So I decided to write my own tool which saves me
time and provides deeper SIP messages content control as well as more robust
message flow control.

# operation
There are three components: pysiptest script, test scenario and message patterns.
pysiptest provides basic operations and helper functions. Test scenario is a
user defined script which provides rules for message flow. It uses helper
functions to send messages. Each message may be preprocessed. The patterns are
used as the basis for messages used by test scenarios

pysiptest.py ---> scenario.py ===> INVITE  --->
                    ^ ^ ^ ^        <---  TRYING
		    | | | |        <--- RINGING
invite.pat ---------+ | | |        <---      OK
ok.pat ---------------+ | |        ACK     --->
ack.pat ----------------+ |        BYE     --->
bye ------------------- --+        <---      OK

# usage
```python pysiptest.py patterns.scenario```
