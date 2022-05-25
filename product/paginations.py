from rest_framework import pagination

class ProductPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'page'

# def ProductPagination(_page_size = 10):
#     class CustomPaginationWithSize(pagination.PageNumberPagination):
#         page_size = _page_size
#         def get_paginated_response(self, data):
#             response = super(CustomPaginationWithSize, self).get_paginated_response(data)
#             response.data['page_size'] = self.page.paginator.num_pages
#             return response
#     return CustomPaginationWithSize