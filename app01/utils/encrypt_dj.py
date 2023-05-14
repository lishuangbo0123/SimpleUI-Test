import hashlib
import random
def calc_md5(password):
      md5_obj = hashlib.md5()
      md5_obj.update(password.encode('utf-8'))
      return md5_obj.hexdigest()


def calc_sha1(password):
    sha1_obj = hashlib.sha1()
    sha1_obj.update(password.encode('utf-8'))
    return sha1_obj.hexdigest()

# 获取由4位随机大小写字母、数字组成的salt值
def create_salt(length=4):
    salt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_chars = len(chars) - 1
    for index in range(length):
        salt += chars[random.randint(0, len_chars)]
    return salt

# 获取原始密码+salt的md5值
def create_md5(pwd, salt):
    md5_obj = hashlib.md5()
    pwd = pwd.encode('utf-8')
    salt = salt.encode('utf-8')
    md5_obj.update(pwd + salt)
    return md5_obj.hexdigest()