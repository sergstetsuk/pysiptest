import sys
import re
import pysiptest
import pysipcall

def State_Idle(pysiptest, event_type, ref): #event_type = timer/message ref = timer_name/message_content
    print '>>> State Processing "%s"' % sys._getframe().f_code.co_name

    pysiptest.pysipcall.ParseMessage(ref)
    if re.search('200', pysiptest.pysipcall.parsed["status"]):
        pysiptest.pysipcall.call["to"] = pysiptest.pysipcall.parsed["to"]
        ack = pysiptest.LoadPattern('patterns/ack.pat')
        pysiptest.SendMessage(ack)
        #pysiptest.SetStateHandler(State_Active)
    return

def Transition_Start(pysiptest):
    print '>>> Transition Processing "%s"' % sys._getframe().f_code.co_name
    pysiptest.pysipcall.call["to"] = "To: <sip:6131@172.24.201.36>"
    notify = pysiptest.LoadPattern('patterns/ua-profile.pat')
    notify = pysiptest.pysipcall.CorrectContentLen(notify)
    pysiptest.SendMessage(notify)
    pysiptest.SetStateHandler(State_Idle);
    return
