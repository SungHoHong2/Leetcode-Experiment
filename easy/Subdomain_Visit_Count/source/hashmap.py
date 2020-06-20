class Solution(object):
    def subdomainVisits(self, cpdomains):

        # create the dictionary that has a value of the counter
        ans = collections.Counter()

        # iterate the domains
        for domain in cpdomains:

            # assign count and domain
            count, domain = domain.split()

            # convert the count to integer
            count = int(count)

            # split the domain
            frags = domain.split('.')
            print(frags, count)

            # iterate through the domain
            for i in range(len(frags)):
                # calculate the total access
                ans[".".join(frags[i:])] += count

        # return the result
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]