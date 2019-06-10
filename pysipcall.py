import re

class PySipCall:
    def ParseMessage(self, msg):
        self.parsed.clear()
        print '>>> ParseMessage'
        for line in msg.splitlines():
            if re.match('^[A-Z]+ sip:.+ SIP/2.0', line):
                self.parsed["method"] = line
            if re.match('^SIP/2.0 \d{3} \S+', line):
                self.parsed["status"] = line
            if re.match('^To: ', line):
                self.parsed["to"] = line
            if re.match('^From: ', line):
                self.parsed["from"] = line
            if re.match('^CSeq: ', line):
                self.parsed["cseq"] = line
            if re.match('^Call-ID: ', line):
                self.parsed["call_id"] = line
            if re.match('^Via: ', line):
                if 'via' in self.parsed:
                    self.parsed["via"] = self.parsed["via"] + "\n" + line
                else:
                    self.parsed["via"] = line
            if len(line) == 0:
                break

        return

    def CorrectContentLen(self, msg):
        bodylen = len(msg) - msg.find("\r\n\r\n") - 4
        contentlen = 'Content-Length: %d' % bodylen
        msg = re.sub('Content-Length: AUTO', contentlen, msg)
        return msg

    def subs_func(self, match):
        key = match.group()[1:-1]
        res = match.group()
        if key in self.call and self.call[key]:
            res = str(self.call[key])
        return res

    def Substitute(self, msg):
        msg = re.sub('\[[a-z_]+\]', self.subs_func, msg)
        return msg

    def ConvertEOLs(self, msg):
        msgtosend = ""
        for line in msg.splitlines():
            msgtosend += line.rstrip('\r\n') + str('\r\n')
        return msgtosend

    def __init__(self, pysiptest):
        self.pysiptest = pysiptest
        self.parsed = {}
        self.call = {
                "call_number": 1,
                "cseq": None,
                "tag": None,
                "branch": None,
                "to": None,
                "from": None,
                "via": None,
                "call_id": None,
                "route": None,
                "contact": None,
                "user-agent": "User-Agent: pysiptest/0.01"
        }
        return

    def __del__(self):
        return
