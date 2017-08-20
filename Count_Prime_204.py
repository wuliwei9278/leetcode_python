class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        ex: 7 => 1,2,3,4,5,6,7
        prime => 2,3,5
        """
        """
        counter = n - 2          
        
        for i in range(2, n):                   #go through every +num (2,3,4,5,6) => n - 2
            for j in range(2,int(i ** 0.5) + 1):            
                if i % j == 0 and i != j:
                    counter -= 1
                    break
                
        if counter  < 0:
            return 0
        
        
        
        return counter                      #pass 18/20 time limit........
        
        """
        """
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in xrange(2, n):
            if res[i] == True:
                for j in xrange(2, (n-1)//i+1):
                    res[i*j] = False
        return sum(res)
        """
        # Sieve of Eratosthenes
        
        if n < 3:
            return 0
        primes = [True]* n        # conduct n true values
        primes[0] = False
        primes[1] = False
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i] = [False]*len(primes[i*i:n:i])
        return sum(primes)
