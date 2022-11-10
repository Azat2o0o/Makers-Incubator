from search import search_object
import json
class CRUDMixin:
    def _get_or_set_objects_and_id(self):
        try:
            if (self.objects or not self.objects) and (self.id or not self.id):
                pass
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0

    def create(self, **kwargs):
        self._get_or_set_objects_and_id()
        self.id += 1
        object_ = dict(id = self.id, **kwargs)
        self.objects.append(object_)
        return {'status': 201, 'msg': object_}

    def list(self):
        result = []
        for obj in self.objects:
            result.append(
                {'id': obj['id'],
                'title': obj['title'],
                'price': obj['price']}
                )
        return {'status': 200, 'msg': self.objects}

    @search_object
    def detail(self, id, **kwargs):
        obj = kwargs['object_']
        if obj:
            return{'status': 200, 'msg': obj}
        return {'status': 404, 'msg': 'Not Found'}

    @search_object
    def update(self, id, **kwargs):
        obj = kwargs.pop('object_')
        if obj:
            obj.update(**kwargs)
            return{'status': 206, 'msg': obj}
        return{'status': 404, 'msg': 'Not found!'}


    @search_object
    def delete(self, id, **kwargs):
        obj = kwargs['object']
        if obj:
            self.objects.remove(obj)
            return {'status': 204, 'msg': 'Successfully deleted!'}
        return {'status': 404, 'msg': 'Not found!'}
    
    def save(self):
        with open('data.json', 'w') as file:
            json.dump(self.objects, file)
        return 'Successfully!'

smartphones = CRUDMixin()
print(smartphones.create(
    title = 'Redmi Note 10',
    description = "Good Phone",
    qty = 10,
    price = 200
))
print(smartphones.create(
    title = 'Redmi Note 11',
    description = "The best phone",
    qty = 3,
    price = 500
))
print(smartphones.create(
    title = 'Iphone 14 Pro MAX',
    description = "NEW PHONE",
    qty = 14,
    price = 1500
))
# print(smartphones.objects)
# print(smartphones.list())
print(smartphones.detail(2))
print(smartphones.save())