# Code Citations

## License: unknown

https://github.com/NathanWorkman/seeker/blob/aa591d412c3954c3cd60bc3217ce7a4a7be71e81/seeker/templates/includes/pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/RomanKhudobei/DiscussIT/blob/a01dcf01c51ee0798de62becaf41bd8d6da76c08/templates/includes/pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/victorgaia/aula4/blob/5c769171809fefbf4c300a09fde7ecb476cc45d6/parciais/_pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: MIT

https://github.com/Bhupesh-V/tutorialdb/blob/b22c948aa573d06551544d9d64053b04bbbfd8d1/app/templates/search_results.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/felipesilvad/dtcgdb/blob/244c743dfd58371edbdbf7efd826b47332eeabf7/cards/templates/cards/cards_list.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: GPL-3.0

https://github.com/sio2project/oioioi/blob/0fcee5ec26341c8820c71d7ea4f104f00e6d7e6f/oioioi/base/templates/pagination/pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: MIT

https://github.com/ltowarek/budget-supervisor/blob/618e01e15a7a76ed870dafccda399720a02b068b/budgetsupervisor/budget/templates/budget/pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/Remus1992/portfolio_webapp/blob/2b146cd37ed0552f145a7aa52eeece1c292098b6/R_E_M/templates/misc/scratch.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/Seredyak1/like_site/blob/1da38d80b306c765be077f4b32524c333f622351/news/templates/news/news.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/rebaza98jira/MainBetaNegocio/blob/a9ca2bf5f8c44072675829f94aa246276c07eb11/betaNegocio/templates/base/base.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/duybtr/tbi/blob/a3a5a7773afd2947b3e3e9353bb928ab7d0f80e1/templates/_base_paginated_results.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/pires1995/web_edtl/blob/6e171c0c0548711156be58291db1b5a4582e6e61/web_edtl/main/templates/inner_page/recruitment/internships_list.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/joanjir/inventarios/blob/882aad98a1a6700d98fe2dccac4546152e0e2909/eltitan/templates/config/Empleadolist.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/fieldsight/fieldsight/blob/aecdb9fb2c23c406ad98256589430bd5217f23da/onadata/apps/fieldsight/templates/fieldsight/donor_site_list.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/luibasantes/AppRadio-Admin/blob/bed759372db15c7fd2b4d6aab5b04c78f69d31e5/AppRadio/WebAdminRadio/templates/webAdminRadio/sugerencias.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/AmarjotSingh21/DjangoBlog/blob/5649e7472cf57253a96de09fee23972aea3ca6b2/templates/posts.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/arasad28/Django-Ecommerce/blob/7b22597b4ad3fff873f0abd31d38dfbf5589d998/templates/home.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/ronybinoy/ShareSphere/blob/93ca7899806cad483fd3e21a19dac4aad3389322/Py/main/Templates/accomodation/acc_propertylist.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: MIT

https://github.com/naritotakizawa/django-easy-uploader/blob/f9df94ebfa3934a45a436eb61b5be614e2f648ab/easy_uploader/templates/easy_uploader/page.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/jAniceto/egichem/blob/0823c24ca172118647327b6f1a837002cf27156f/lab/templates/lab/inventory.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}{
```

## License: unknown

https://github.com/NathanWorkman/seeker/blob/aa591d412c3954c3cd60bc3217ce7a4a7be71e81/seeker/templates/includes/pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/Seredyak1/like_site/blob/1da38d80b306c765be077f4b32524c333f622351/news/templates/news/news.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/arnaudflorence/BlogPython/blob/78d682cd447b6abfdf38eb31e90a8e84ca838c44/acme/blog/templates/blog/index.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/AmarjotSingh21/DjangoBlog/blob/5649e7472cf57253a96de09fee23972aea3ca6b2/templates/posts.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/andrey-gl/studygram/blob/112350689922029879ece4e296bd492073c6a243/templates/inc/_pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/fieldsight/fieldsight/blob/aecdb9fb2c23c406ad98256589430bd5217f23da/onadata/apps/fieldsight/templates/fieldsight/organization_list.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/ahmrudi/xyz/blob/6fb7a2d39dbe879e5303e665847083d46606f5a2/sia/templates/brankas/index.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/victorgaia/aula4/blob/5c769171809fefbf4c300a09fde7ecb476cc45d6/parciais/_pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/arasad28/Django-Ecommerce/blob/7b22597b4ad3fff873f0abd31d38dfbf5589d998/templates/home.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/pires1995/web_edtl/blob/6e171c0c0548711156be58291db1b5a4582e6e61/web_edtl/main/templates/inner_page/recruitment/internships_list.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/ronybinoy/ShareSphere/blob/93ca7899806cad483fd3e21a19dac4aad3389322/Py/main/Templates/accomodation/acc_propertylist.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/joanjir/inventarios/blob/882aad98a1a6700d98fe2dccac4546152e0e2909/eltitan/templates/config/Empleadolist.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: GPL-3.0

https://github.com/sio2project/oioioi/blob/0fcee5ec26341c8820c71d7ea4f104f00e6d7e6f/oioioi/base/templates/pagination/pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/alkyl1978/django_site/blob/8d32973e8762e60b152d44f2b5831e254865d1f1/blog/templates/blog/post_list.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/pires1995/web_edtl/blob/6e171c0c0548711156be58291db1b5a4582e6e61/web_edtl/main/templates/inner_page/recruitment/internships_list.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/ronybinoy/ShareSphere/blob/93ca7899806cad483fd3e21a19dac4aad3389322/Py/main/Templates/accomodation/acc_propertylist.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/joanjir/inventarios/blob/882aad98a1a6700d98fe2dccac4546152e0e2909/eltitan/templates/config/Empleadolist.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: GPL-3.0

https://github.com/sio2project/oioioi/blob/0fcee5ec26341c8820c71d7ea4f104f00e6d7e6f/oioioi/base/templates/pagination/pagination.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/alkyl1978/django_site/blob/8d32973e8762e60b152d44f2b5831e254865d1f1/blog/templates/blog/post_list.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/MakChan/noticeboard/blob/4cc8513f34e518fe7351ffadcad7ce68a5ddb0a9/notices/templates/notices/home.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/Seredyak1/like_site/blob/1da38d80b306c765be077f4b32524c333f622351/news/templates/news/news.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/arnaudflorence/BlogPython/blob/78d682cd447b6abfdf38eb31e90a8e84ca838c44/acme/blog/templates/blog/index.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/victorgaia/aula4/blob/5c769171809fefbf4c300a09fde7ecb476cc45d6/parciais/_pagination.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/andrey-gl/studygram/blob/112350689922029879ece4e296bd492073c6a243/templates/inc/_pagination.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/arasad28/Django-Ecommerce/blob/7b22597b4ad3fff873f0abd31d38dfbf5589d998/templates/home.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/fieldsight/fieldsight/blob/aecdb9fb2c23c406ad98256589430bd5217f23da/onadata/apps/fieldsight/templates/fieldsight/organization_list.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/ahmrudi/xyz/blob/6fb7a2d39dbe879e5303e665847083d46606f5a2/sia/templates/brankas/index.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/AmarjotSingh21/DjangoBlog/blob/5649e7472cf57253a96de09fee23972aea3ca6b2/templates/posts.html

```
4">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/fieldsight/fieldsight/blob/aecdb9fb2c23c406ad98256589430bd5217f23da/onadata/apps/fieldsight/templates/fieldsight/organization_list.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/ahmrudi/xyz/blob/6fb7a2d39dbe879e5303e665847083d46606f5a2/sia/templates/brankas/index.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/NathanWorkman/seeker/blob/aa591d412c3954c3cd60bc3217ce7a4a7be71e81/seeker/templates/includes/pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/Seredyak1/like_site/blob/1da38d80b306c765be077f4b32524c333f622351/news/templates/news/news.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/arnaudflorence/BlogPython/blob/78d682cd447b6abfdf38eb31e90a8e84ca838c44/acme/blog/templates/blog/index.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/victorgaia/aula4/blob/5c769171809fefbf4c300a09fde7ecb476cc45d6/parciais/_pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/AmarjotSingh21/DjangoBlog/blob/5649e7472cf57253a96de09fee23972aea3ca6b2/templates/posts.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/andrey-gl/studygram/blob/112350689922029879ece4e296bd492073c6a243/templates/inc/_pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/arasad28/Django-Ecommerce/blob/7b22597b4ad3fff873f0abd31d38dfbf5589d998/templates/home.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/pires1995/web_edtl/blob/6e171c0c0548711156be58291db1b5a4582e6e61/web_edtl/main/templates/inner_page/recruitment/internships_list.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/ronybinoy/ShareSphere/blob/93ca7899806cad483fd3e21a19dac4aad3389322/Py/main/Templates/accomodation/acc_propertylist.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/joanjir/inventarios/blob/882aad98a1a6700d98fe2dccac4546152e0e2909/eltitan/templates/config/Empleadolist.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: GPL-3.0

https://github.com/sio2project/oioioi/blob/0fcee5ec26341c8820c71d7ea4f104f00e6d7e6f/oioioi/base/templates/pagination/pagination.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```

## License: unknown

https://github.com/alkyl1978/django_site/blob/8d32973e8762e60b152d44f2b5831e254865d1f1/blog/templates/blog/post_list.html

```
-5">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                    <i class="bi bi-chevron-left"></i>
                </a>
            </li>
            {% endif %}

            {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
            <li class="page-item active">
                <span class="page-link">{{ num }}</span>
            </li>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <li class="page-item">
                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
            </li>
            {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                    <i class="bi bi-chevron-right"></i>
                </a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %
```
