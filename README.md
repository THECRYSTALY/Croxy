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
requester.set_proxy('your_proxy_address', 8080)

# Make a request using the configured proxy
response = requester.get('https://example.com')

print('Response:', response.text)
```

## Configuration

The package supports the following configuration options:

- **Proxy Address:** The address of the proxy server.
- **Proxy Port:** The port number on which the proxy server is running.

Example configuration:

```python
requester.set_proxy('proxy.example.com', 8080)
```

## Examples

### Making GET Request

```python
response = requester.get('https://example.com')
print('Response:', response.text)
```

### Making POST Request

```python
post_data = {'key1': 'value1', 'key2': 'value2'}

response = requester.post('https://api.example.com', data=post_data)
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
