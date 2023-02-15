from urllib.parse import urlparse


# Get subdomain name (names.example.com)
def get_subdomain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ""


# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_subdomain_name(url).split(".")
        length = len(results)
        if length == 3:
            return f"{results[-2]}.{results[-1]}"
        else:
            return f"{results[-3]}.{results[-2]}.{results[-1]}"
    except:
        return ""
