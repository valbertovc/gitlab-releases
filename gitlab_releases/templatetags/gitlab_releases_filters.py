from django import template

register = template.Library()


@register.filter
def release_section_css(section):
    items = {
        "added": "success",
        "changed": "info",
        "fixed": "warning",
        "removed": "danger",
    }
    return items.get(section, "info")
