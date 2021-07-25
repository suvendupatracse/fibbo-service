def get_n_fibbo(n: int)-> int:
        fibbo_series = []
        if n < 0:
            raise ValueError("Invalid number")
        elif n == 0:
            fibbo_series.append(0)
        elif n == 1:
            fibbo_series.append(1)
        else:
            for i in range(n+1):
                if i == 0:
                    fibbo_series.append(0)
                elif i == 1:
                    fibbo_series.append(1)
                else:
                    fibbo_series.append(fibbo_series[i-1]+ fibbo_series[i-2])
        return fibbo_series[-1]
