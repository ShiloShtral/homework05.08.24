def prform_action(action):
    actions = {
        'add': 'Adding item',
        'delete': 'Deleting item',
        'update': 'Updating item'
    }
    return actions.get(action,'Unkown action')
result = prform_action('add')
print(result)