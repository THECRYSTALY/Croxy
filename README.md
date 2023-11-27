# Croxy Package

The Croxy package is a Python library that enables developers to send HTTP requests through a proxy server effortlessly. This package provides a simple and configurable interface, allowing users to set the proxy address and port according to their specific needs.

## Features

- **Proxy Support:** Easily send HTTP requests through a proxy server.
- **Configurability:** Set the proxy address and port with ease.
- **Compatibility:** Works seamlessly with various HTTP libraries and frameworks.
- **Ease of Use:** Minimal setup for quick integration into existing projects.

## Installation

## Usage

```python
from croxy.client import HTTProxy

# Create an instance of HTTProxy
requester = HTTProxy()

# Set proxy configuration
requester.set_proxy(('your_proxy_address', 8080))

# Make a request using the configured proxy
response = requester.get('https://example.com')

print('Response:', response.text)
```

## Examples

### Porxy With Sessions Support 

```python
from croxy.client import Proxy

proxy = Proxy(session=True)
proxy.set_proxy(('your_proxy_address','your_proxy_port'))
proxy.post('https://example.com/login', data={ 'username': 'admin', 'password': 'admin' }
response = proxy.get('https://example.com/user')
print('Response:', response.text)
```

### Proxy That Requires Authentication

```python
from croxy.client import Proxy

proxy = Proxy()
proxy.set_proxy(('your_proxy_address','your_proxy_port'), ('your_username','your_password'))
response = proxy.get('https://example.com/user')
print('Response:', response.text)
```

## TODO

- **Proxy Server:** Easily, create a proxy server.
- **More Protocols:** Add support for other protocols.

## Contribution

Feel free to contribute to the development of this package by submitting issues or pull requests on the [GitHub repository](https://github.com/THECRYSTALY/Croxy).

## License

This package is licensed under the [MIT License](LICENSE).

Happy coding!
