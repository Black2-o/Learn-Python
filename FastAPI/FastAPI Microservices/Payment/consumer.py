from main import redis, Order
import time

key = 'refund_order'
group = 'payment_group'


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
                obj = res[1][0][1]
                order = Order.get(obj['pk'])
                order.status = 'refunded'
                order.save()
    except Exception as e:
        # print(str(e))
        pass
    time.sleep(1)