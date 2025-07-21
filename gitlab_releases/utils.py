import functools

from django.core.cache import cache


def memoize(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        class_name = self.__class__.__name__
        method_name = method.__name__
        key = f"{class_name}:{method_name}".lower()
        key_args = ",".join(map(str, args))
        if key_args:
            key += f":{key_args}"
        key_kwargs = ",".join(f"{k}={v}" for k, v in kwargs.items())
        if key_kwargs:
            key += f":{key_kwargs}"
        result = cache.get(key)
        if result is not None:
            return result
        result = method(self, *args, **kwargs)
        cache.set(key, result)
        return result

    return wrapper
