class CallableComponent:
    def __init__(self, element_type, **kwargs):
        self.element_class = element_type
        self.kwargs = kwargs

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.element_class(page=instance.page, instance=instance, **self.kwargs)


def locate(element_type, **kwargs):
    def decorator(func):
        return CallableComponent(element_type=element_type, **kwargs)
    return decorator
