import requests
from requests.auth import HTTPProxyAuth


class HTTProxy:
    
    TEST_URL = 'http://httpbin.org/ip'

    def __init__(self, session: bool = False):
        """
        session: set it to True if you want to save tokens and cookies.
        """
        self.requests = requests.Session() if session else requests
        self.auth = None
        self.proxy = None
    
    def set_proxy(self, address, auth=None):
        """
        call it if you want to use a proxy, otherwise requests will use the system`s ip address.
        address: Tuple of form (address, port).
        auth: Tuple of form (username,password)
        """
        addr, port = address
        if auth:
            self.auth = HTTPProxyAuth(auth[0], auth[1])
        self.proxy = (address, port)

    def test(self):
        """
        Tests the proxy using TEST_URL.
        """
        proxy = {
            "http": f"http://{self.proxy[0]}:{self.proxy[1]}",
        } if self.proxy else None
        try:
            response = self.requests.get(self.TEST_URL, proxies=proxy, auth=self.auth)
            if response.status_code == 200:
                return True
        except:
            pass
        return False

    def post(self, *args, **kwargs):
        """
        Sends a post request using the proxy.
        """
        proxy = {
            "http": f"{self.proxy[0]}:{self.proxy[1]}",
        } if self.proxy else None

        try:
            response = self.requests.post(*args, proxies=proxy, auth=self.auth, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e

    def get(self, *args, **kwargs):
        """
        Sends a get request using the proxy.
        """
        proxy = {
            "http": f"{self.proxy[0]}:{self.proxy[1]}",
        } if self.proxy else None

        try:
            response = self.requests.get(*args, proxies=proxy, auth=self.auth, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e
    
    def put(self, *args, **kwargs):
        """
        Sends a put request using the proxy.
        """
        proxy = {
            "http": f"{self.proxy[0]}:{self.proxy[1]}",
        } if self.proxy else None

        try:
            response = self.requests.put(*args, proxies=proxy, auth=self.auth, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e
    
    def delete(self, *args, **kwargs):
        """
        Sends a delete request using the proxy.
        """
        proxy = {
            "http": f"{self.proxy[0]}:{self.proxy[1]}",
        } if self.proxy else None

        try:
            response = self.requests.delete(*args, proxies=proxy, auth=self.auth, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e
    
    def patch(self, *args, **kwargs):
        """
        Sends a get request using the proxy.
        """
        proxy = {
            "http": f"{self.proxy[0]}:{self.proxy[1]}",
        } if self.proxy else None

        try:
            response = self.requests.patch(*args, proxies=proxy, auth=self.auth, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e
    
    def head(self, *args, **kwargs):
        """
        Sends a head request using the proxy.
        """
        proxy = {
            "http": f"{self.proxy[0]}:{self.proxy[1]}",
        } if self.proxy else None

        try:
            response = self.requests.head(*args, proxies=proxy, auth=self.auth, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e
    
    def options(self, *args, **kwargs):
        """
        Sends an options request using the proxy.
        """
        proxy = {
            "http": f"{self.proxy[0]}:{self.proxy[1]}",
        } if self.proxy else None

        try:
            response = self.requests.options(*args, proxies=proxy, auth=self.auth, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e