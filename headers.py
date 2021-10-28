import time
class GeneralHeader:
    def __init__(self, connection='Not Defined', tran_enco='Not Defined', alive='Not Defined'):
        self.Date = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.gmtime())
        self.Transfer_Encoding = tran_enco
        self.Connection = connection
        self.Keep_Alive = alive
        self.genhead = dict()
        self.genhead.update({'Date' : self.Date, 'Connection' : self.Connection, 'Keep-Alive' : self.Keep_Alive})
        
    def general_header(self):
        gh = ""
        for x, y in self.genhead.items():
            if y != 'Not Defined':
                gh += str(x) + ': ' + str(y) + "\r\n"
        return gh


class EntityHeader:
    def __init__(self, con_enco = 'Not Defined', con_ty = 'text/html', con_len = 'Not Defined', last_mod = 'Not Defined', con_loc = 'Not Defined', exp = 'Not Defined', allow = 'Not Defined', con_md5 = 'Not Defined'):
        self.Content_Encoding = con_enco
        self.Content_MD5 = con_md5
        self.Content_Length = con_len
        self.Expires = exp
        self.Last_Modified = last_mod
        self.Content_Location = con_loc
        self.Allow = allow
        self.Content_Type = con_ty

    def entity_header(self):
        return '\r\nAllow: ' + self.Allow + '\r\nExpires: ' + self.Expires + '\r\nLast-Modified: ' + self.Last_Modified + '\r\nContent-Encoding: ' + self.Content_Encoding + '\r\nContent-Type: ' + self.Content_Type + '\r\nContent-Length: ' + self.Content_Length + '\r\nContent-Location: ' + self.Content_Location + '\r\nContent-MD5: ' + self.Content_MD5


class RequestHeader:
    def __init__(self, host='Not Defined', user='Not Defined', acpt='Not Defined', acpt_enco='Not Defined', acpt_char='Not Defined', range='Not Defined', if_mod_sin='Not Defined', if_ran='Not Defined', if_unmod_sin='Not Defined'):
        self.User = user
        self.Host = host
        self.Range = range
        self.Accept = acpt
        self.Accept_Charset = acpt_char
        self.Accept_Encoding = acpt_enco
        self.If_Modified_Since = if_mod_sin
        self.If_Range = if_ran
        self.If_Unmodified_Since = if_unmod_sin

    
    def request_header(self):
        rh = '\r\nUser: ' + self.User + '\r\nHost: ' + self.Host + '\r\nRange: ' + self.Range + '\r\nAccept: ' + self.Accept + '\r\nAccept-Charset: ' + self.Accept_Charset + '\r\nAccept-Encoding: ' + self.Accept_Encoding + '\r\nIf_Modified_Since: ' + self.If_Modified_Since + '\r\nIf-Range: ' + self.If_Range + '\r\nIf_Unmodified_Since: ' + self.If_Unmodified_Since
        
        return rh   


status_codes = {
        100:'Continue',
        101:'Switching Protocols',
        103:'Early Hints',
        200:'OK',
        201:'Created',
        202:'Accepted',
        203:'Non - Authoritative Information',
        204:'No Content',
        205:'Reset Content',
        206:'Partial Content',
        300:'Multiple Choices',
        301:'Moved Permanently',
        302:'Found',
        303:'See Other',
        304:'Not Modified',
        307:'Temporary Redirect',
        308:'Permanent Redirect',
        400:'Bad Request',
        401:'Unauthorized',
        402:'Payment Required',
        403:'Forbidden',
        404:'Not Found',
        405:'Method Not Allowed',
        406:'Not Acceptable',
        407:'Proxy AuthenticationRequired',
        408:'Request Timeout',
        409:'Conflict',
        410:'Gone',
        411:'Length Required',
        412:'Precondition Failed',
        413:'Payload Too Large',
        414:'URI Too Long',
        415:'Unsupported Media Type',
        416:'Range Not Satisfiable',
        417:'Expectation Failed',
        418:'I\'m a teapot',
        422:'Unprocessable Entity',
        425:'Too Early',
        426:'Upgrade Required',
        428:'Precondition Required',
        429:'Too Many Requests',
        431:'Request Header Fields Too Large',
        451:'Unavailable For Legal Reasons',
        500:'Internal Server Error',
        501:'Not Implemented',
        502:'Bad Gateway',
        503:'Service Unavailable',
        504:'Gateway Timeout',
        505:'HTTP Version Not Supported',
        506:'Variant Also Negotiates',
        507:'Insufficient Storage',
        508:'Loop Detected',
        510:'Not Extended',
        511:'Network Authentication Required'
    }