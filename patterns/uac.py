import sys
import re
import pysiptest
import pysipcall

def State_Active(pysiptest, event_type, ref):
    print '>>> State Processing "%s"' % sys._getframe().f_code.co_name

    pysiptest.pysipcall.ParseMessage(ref)
    if re.search('BYE', pysiptest.pysipcall.parsed["method"]):
        pysiptest.pysipcall.call["to"] = pysiptest.pysipcall.parsed["to"]
        pysiptest.pysipcall.call["from"] = pysiptest.pysipcall.parsed["from"]
        pysiptest.pysipcall.call["via"] = pysiptest.pysipcall.parsed["via"]
        pysiptest.pysipcall.call["call_id"] = pysiptest.pysipcall.parsed["call_id"]
        pysiptest.pysipcall.call["cseq"] = pysiptest.pysipcall.parsed["cseq"]
        ok = pysiptest.LoadPattern('patterns/ok.pat')
        pysiptest.SendMessage(ok)
        #pysiptest.SetStateHandler(State_Idle)
        #Transition_Start(pysiptest)
    return

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
    invite = pysiptest.LoadPattern('patterns/invite.pat')
    pysiptest.SendMessage(invite)
    pysiptest.SetStateHandler(State_Idle);
    return
