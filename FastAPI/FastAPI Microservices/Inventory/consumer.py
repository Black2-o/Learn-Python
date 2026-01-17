from main import redis, Product
import time

key = 'order_completed'
group = 'inventory_group'


try:
    redis.xgroup_create(key, group)
except:
    print('Group already exists')


while True:
    try:
        result = redis.xreadgroup(group, 'consumer-1', {key: '>'}, None)
        if result != []:
            print(result)
            
        if result != []:
            for res in result:
                objects = res[1][0][1]
                try:
                    product = Product.get(objects['product_id'])
                    product.quantity = product.quantity - int(objects['quantity'])
                    product.save() 
                except:
                    redis.xadd('refund_order', objects, '*')
    except Exception as e:
        # print(str(e))
        pass
    time.sleep(1)