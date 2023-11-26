import requests


class Proxy:

    TEST_URL = 'http://httpbin.org/ip'

    def __init__(self, address, port, session=False, proxy=True, auto_test=True):
        self.address = address
        self.port = port
        self.proxy = proxy
        self.requests = requests.Session() if session else requests
        self.valid = self.test() if auto_test else None

    def test(self):
        """
        Tests the proxy using TEST_URL, used to set the proxy valid or invalid.

        :return: Boolean.

        todo add support for other protocols.
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

        :param args: Same args that requests.post take.
        :param kwargs: same kwargs that requests.post take.
        :return: Tuple
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

        :param args: Same args that requests.get take.
        :param kwargs: same kwargs that requests.get take.
        :return: Tuple
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

        :param args: Same args that requests.put take.
        :param kwargs: same kwargs that requests.put take.
        :return: Tuple
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

        :param args: Same args that requests.delete take.
        :param kwargs: same kwargs that requests.delete take.
        :return: Tuple
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

        :param args: Same args that requests.patch take.
        :param kwargs: same kwargs that requests.patch take.
        :return: Tuple
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

        :param args: Same args that requests.head take.
        :param kwargs: same kwargs that requests.head take.
        :return: Tuple
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

        :param args: Same args that requests.options take.
        :param kwargs: same kwargs that requests.options take.
        :return: Tuple
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