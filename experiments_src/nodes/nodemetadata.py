from distributions.distributions import BaseDistribution


class NodeMetadata:

    def __init__(self,
                 up_distribution: BaseDistribution,
                 down_distribution: BaseDistribution):
        self.status = 'UP'
        self.up_distribution = up_distribution
        self.down_distribution = down_distribution
        self.time_left = self.up_distribution.next()

    def tick(self):
        self.time_left -= 1

        if self.time_left <= 0:
            self.status_change()

    def status_change(self):
        if self.status == 'UP':
            self.status = 'DOWN'
            self.time_left = self.down_distribution.next()
            return
        if self.status == 'DOWN':
            self.status = 'UP'
            self.time_left = self.up_distribution.next()
            return

    def __str__(self):
        return self.status + ':  ' + str(self.time_left)
