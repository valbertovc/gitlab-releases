from functools import cached_property

from django.core.paginator import Page, Paginator


class GitlabPaginator(Paginator):
    def page(self, number):
        return self._get_page(self.object_list, number, self)

    def _get_page(self, *args, **kwargs):
        return GitlabPage(*args, **kwargs)

    @cached_property
    def count(self):
        return len(self.object_list) * 2


class GitlabPage(Page):
    def __len__(self):
        return len(self.object_list) * 2

    def has_next(self):
        return True if self.object_list else False

    def next_page_number(self):
        return self.number + 1

    def previous_page_number(self):
        return self.number - 1
