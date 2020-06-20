class Solution(object):
    def subdomainVisits(self, cpdomains):

        # create the dictionary that has a value of the counter
        visitMap = {}

        # iterate the domains
        for domain in cpdomains:

            # assign count and domain
            count, domain = domain.split(' ')[0], domain.split(' ')[1]

            # convert the count to integer
            count = int(count)

            # split the domain and iterate the subdomains
            subdomains = domain.split('.')
            for i in range(len(subdomains)):

                # generate the subdomains
                subdomain = ".".join(subdomains[i:])

                # calculate the total access
                if subdomain not in visitMap:
                    visitMap[subdomain] = count
                else:
                    visitMap[subdomain] += count

        return ["{} {}".format(count, domain) for domain, count in visitMap.items()]
