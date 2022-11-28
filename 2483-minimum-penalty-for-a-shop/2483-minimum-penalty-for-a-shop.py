class Solution(object):
    def bestClosingTime(self, customers):
        beg = customers.count('Y')
        end = customers.count('N')
        min_p = beg if beg <= end else end
        l_hr = 0 if beg <= end else len(customers)
        prev_y = 0
        prev_n = 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                prev_y += 1
            else:
                prev_n += 1
            p_at_now = prev_n + beg - prev_y
            if p_at_now == min_p and i+1 < l_hr:
                l_hr = i + 1
            elif p_at_now < min_p:
                min_p = p_at_now
                l_hr = i + 1

        return l_hr