from edition.models import Sort, Edition

NUM_ITEMS_PER_PAGE = 5

SORT = Sort.objects.filter(disabled=False)
EDITION = Edition.objects.filter(disabled=False)

MENU = []
for sort in SORT:
    items = [sort]
    items.extend(list(Edition.objects.filter(sort=sort, disabled=False)))
    MENU.append(items)

# Constants available for templates
def showConstants(request):
    context = {
        'SORT':SORT, 
        'EDITION':EDITION,
        'MENU':MENU
}
    return context
    