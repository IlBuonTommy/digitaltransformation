'''
Flower model class to represent flower data and sample flower dataset.
'''
class Flower:
    def __init__(self, name, price, image_url, description):
        self.name = name
        self.price = price
        self.image_url = image_url
        self.description = description
# Sample flower data (in a real application this would come from a database)
flowers_data = [
    {
        'name': 'Rose',
        'price': 2.99,
        'image_url': 'https://example.com/rose.jpg',
        'description': 'Classic red roses for your special someone.'
    },
    {
        'name': 'Tulip',
        'price': 1.49,
        'image_url': 'https://example.com/tulip.jpg',
        'description': 'Bright and colorful tulips in a variety of shades.'
    },
    {
        'name': 'Lily',
        'price': 3.99,
        'image_url': 'https://example.com/lily.jpg',
        'description': 'Elegant lilies for a touch of sophistication.'
    }
]