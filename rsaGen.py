__author__ = 'piyush sohal'

import rsa

(pub_key, priv_key) = rsa.newkeys(512)
pub = pub_key._save_pkcs1_pem()
priv = priv_key._save_pkcs1_pem()
file = open('E:\WAREZ\PycharmProjects\PixelProcess\pubkey.pem', 'wb')
file.write(pub)
file.close()
file = open('E:\WAREZ\PycharmProjects\PixelProcess\privkey.pem', 'wb')
file.write(priv)
file.close()