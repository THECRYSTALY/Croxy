import requests


class HTTProxy:
    """
    class for HTTP prxoy.
    """
    TEST_URL = 'http://httpbin.org/ip'

    def __init__(self, address: str, port: int = 80, session: bool = False, proxy: bool = True, auto_test: bool = True):
        """
        address: the address of the proxy.
        port: port of the proxy, default is 80.
        session: set it to True if you want to save token and cookies.
        proxy: set it to False if you dont want a proxy to be used.
        auto_test: automatically tests the proxy, set it to False if you dont want that.
        """
        self.address = address
        self.port = port
        self.proxy = proxy
        self.requests = requests.Session() if session else requests
        self.valid = self.test() if auto_test else None

    def test(self):
        """
        Tests the proxy using TEST_URL, used to set the proxy valid or invalid.
        """
        proxy = {
            "http": f"http://{self.address}:{self.port}",
        } if self.proxy else None
        try:
            response = self.requests.get(self.TEST_URL, proxies=proxy)
            if response.status_code == 200:
                return True
        except:
            pass
        return False

    def post(self, *args, **kwargs):
        """
        Sends a post request using the proxy.

        args: Same args that requests.post take.
        kwargs: same kwargs that requests.post take.
        """
        proxy = {
            "http": f"{self.address}:{self.port}",
        } if self.proxy else None

        try:
            response = self.requests.post(*args, proxies=proxy, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e

    def get(self, *args, **kwargs):
        """
        Sends a get request using the proxy.

        args: Same args that requests.get take.
        kwargs: same kwargs that requests.get take.
        """
        proxy = {
            "http": f"{self.address}:{self.port}",
        } if self.proxy else None

        try:
            response = self.requests.get(*args, proxies=proxy, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e
    
    def put(self, *args, **kwargs):
        """
        Sends a put request using the proxy.

        args: Same args that requests.put take.
        kwargs: same kwargs that requests.put take.
        """
        proxy = {
            "http": f"{self.address}:{self.port}",
        } if self.proxy else None

        try:
            response = self.requests.put(*args, proxies=proxy, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e
    
    def delete(self, *args, **kwargs):
        """
        Sends a delete request using the proxy.

        args: Same args that requests.delete take.
        kwargs: same kwargs that requests.delete take.
        """
        proxy = {
            "http": f"{self.address}:{self.port}",
        } if self.proxy else None

        try:
            response = self.requests.delete(*args, proxies=proxy, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e
    
    def patch(self, *args, **kwargs):
        """
        Sends a get request using the proxy.

        args: Same args that requests.patch take.
        kwargs: same kwargs that requests.patch take.
        """
        proxy = {
            "http": f"{self.address}:{self.port}",
        } if self.proxy else None

        try:
            response = self.requests.patch(*args, proxies=proxy, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e
    
    def head(self, *args, **kwargs):
        """
        Sends a head request using the proxy.

        args: Same args that requests.head take.
        kwargs: same kwargs that requests.head take.
        """
        proxy = {
            "http": f"{self.address}:{self.port}",
        } if self.proxy else None

        try:
            response = self.requests.head(*args, proxies=proxy, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e
    
    def options(self, *args, **kwargs):
        """
        Sends a options request using the proxy.

        args: Same args that requests.options take.
        kwargs: same kwargs that requests.options take.
        """
        proxy = {
            "http": f"{self.address}:{self.port}",
        } if self.proxy else None

        try:
            response = self.requests.options(*args, proxies=proxy, **kwargs)
            return 0, response
        except requests.exceptions.ProxyError as e:
            return 1, e
        except Exception as e:
            return 2, e