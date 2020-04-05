import time


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ttcapacity = capacity
        self.d = {

        }

    def get(self, key: int) -> int:
        try:
            v = self.d[key]['value']
            self.d[key]['t'] = self.d[key]['t'] + 1
            self.d[key]['last_use'] = time.time()
            return v
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.ttcapacity == 0:
            return None
        if key in self.d.keys():
            self.d[key]['value'] = value
            self.d[key]['t'] = self.d[key]['t'] + 1
            self.d[key]['last_use'] = time.time()
            return None
        if self.capacity > 0:
            self.d[key] = {'value': value, 't': 1, 'last_use': time.time()}
            self.capacity = self.capacity - 1
        else:
            tmp_key = ''
            tmp_t = 9999
            tmp_time = 2586078464
            for k in self.d.keys():
                if self.d[k]['t'] < tmp_t:
                    tmp_t = self.d[k]['t']
                    tmp_key = k
                    tmp_time = self.d[k]['last_use']
                elif self.d[k]['t'] == tmp_t:
                    if self.d[k]['last_use'] < tmp_time:
                        tmp_time = self.d[k]['last_use']
                        tmp_key = k
                        tmp_t = self.d[k]['t']

            self.d.pop(tmp_key)
            self.d[key] = {'value': value, 't': 1, 'last_use': time.time()}
